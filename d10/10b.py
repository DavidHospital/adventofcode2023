from typing import Dict, List, Tuple


NORTH = (0, -1)
SOUTH = (0, 1)
WEST = (-1, 0)
EAST = (1, 0)


PIPE_CONNECTIONS = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
}


# .....
# .F-7.
# .|.|.
# .L-J.
# .....

COLOR_TABLE: Dict[Tuple[str, Tuple[int, int]], Dict[Tuple[int, int], bool]] = {
        ("|", NORTH): {EAST: True, WEST: False},
        ("|", SOUTH): {EAST: False, WEST: True},
        ("-", WEST): {NORTH: True, SOUTH: False},
        ("-", EAST): {NORTH: False, SOUTH: True},
        ("L", NORTH): {WEST: False, SOUTH: False},
        ("L", EAST): {WEST: True, SOUTH: True},
        ("J", NORTH): {EAST: True, SOUTH: True},
        ("J", WEST): {EAST: False, SOUTH: False},
        ("7", SOUTH): {EAST: False, NORTH: False},
        ("7", WEST): {EAST: True, NORTH: True},
        ("F", EAST): {WEST: False, NORTH: False},
        ("F", SOUTH): {WEST: True, NORTH: True},
}


CONNECTION_PIPES = {
    (NORTH, SOUTH): "|",
    (SOUTH, NORTH): "|",
    (EAST, WEST): "-",
    (WEST, EAST): "-",
    (NORTH, EAST): "L",
    (EAST, NORTH): "L",
    (NORTH, WEST): "J",
    (WEST, NORTH): "J",
    (SOUTH, WEST): "7",
    (WEST, SOUTH): "7",
    (SOUTH, EAST): "F",
    (EAST, SOUTH): "F",
}


DIRECTIONS = [EAST, WEST, NORTH, SOUTH]

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
ENDC = '\033[0m'


class Maze:
    def __init__(self, lines: List[str]):
        self.lines = lines
        self.width: int = len(lines[0])
        self.height: int = len(lines)
        self.start_y: int = next(idx for idx, line in enumerate(lines) if "S" in line)
        self.start_x: int = next(idx for idx, char in enumerate(lines[self.start_y]) if char == "S")

    def get_start(self) -> Tuple[int, int]:
        return (self.start_x, self.start_y)

    def in_bounds(self, x, y) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x: int, y: int) -> str:
        if not 0 <= x <= self.width or not 0 <= y <= self.height:
            return "."

        # start logic
        if x == self.start_x and y == self.start_y:
            neighbours = []
            for (dx, dy) in DIRECTIONS:
                neighbour = self.get(x + dx, y + dy)
                if neighbour in PIPE_CONNECTIONS and any(dx + di == 0 and dy + dj == 0 for (di, dj) in PIPE_CONNECTIONS[neighbour]):
                    neighbours.append((dx, dy))
            assert len(neighbours) == 2
            return CONNECTION_PIPES[(neighbours[0], neighbours[1])]
        return self.lines[y][x]


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    maze = Maze(lines)
    
    start_shape = maze.get(maze.start_x, maze.start_y)
    starting_dir = PIPE_CONNECTIONS[start_shape][0]
    maze_tiles: Dict[Tuple[int, int], Tuple[int, int]] = {(maze.start_x, maze.start_y): starting_dir}
    queue: List[Tuple[int, int]] = [(maze.start_x + starting_dir[0], maze.start_y + starting_dir[1])]
    while len(queue) > 0:
        (x, y) = queue.pop(0)
        tile = maze.get(x, y)
        dirs = PIPE_CONNECTIONS[tile]
        traveling_dir = next(((dx, dy) for (dx, dy) in dirs if (x + dx, y + dy) not in maze_tiles), None)
        if traveling_dir is None:
            traveling_dir = next((dx, dy) for (dx, dy) in dirs if (x + dx, y + dy) == (maze.start_x, maze.start_y))
        else:
            queue.append((x + traveling_dir[0], y + traveling_dir[1]))
        maze_tiles[(x, y)] = traveling_dir

    color_yes = []
    color_no = []
    for y in range(maze.height):
        for x in range(maze.width):
            if (x, y) in maze_tiles:
                continue
            colored = False
            for dir in DIRECTIONS:
                (i, j) = (x, y)
                while maze.in_bounds(i, j):
                    if (i, j) in maze_tiles:
                        if COLOR_TABLE[(maze.get(i, j), maze_tiles[(i, j)])][(dir[0] * -1, dir[1] * -1)]:
                            color_yes.append((x, y))
                        else:
                            color_no.append((x, y))
                        colored = True 
                        break
                    (i, j) = (i + dir[0], j + dir[1])
                if colored:
                    break
            
    print(len(color_yes))
    print(len(color_no))

    print(maze_tiles)
    for y in range(maze.height):
        for x in range(maze.width):
            if (x, y) in color_no:
                print(RED + maze.get(x, y) + ENDC, end="")
            elif (x, y) in maze_tiles:
                print(GREEN + maze.get(x, y) + ENDC, end="")
            else:
                print(maze.get(x, y), end="")
        print()
        



            
