from functools import reduce
import operator
from typing import List, Tuple


PIPE_CONNECTIONS = {
    "|": [(0,-1), (0,1)],
    "-": [(-1,0), (1,0)],
    "L": [(0,-1), (1,0)],
    "J": [(0,-1), (-1,0)],
    "7": [(0,1), (-1,0)],
    "F": [(0,1), (1,0)],
}


CONNECTION_PIPES = {
    ((0,-1), (0,1)): "|",
    ((0,1), (0,-1)): "|",
    ((-1,0), (1,0)): "-",
    ((1,0), (-1,0)): "-",
    ((0,-1), (1,0)): "L",
    ((1,0), (0,-1)): "L",
    ((0,-1), (-1,0)): "J",
    ((-1,0), (0,-1)): "J",
    ((0,1), (-1,0)): "7",
    ((-1,0), (0,1)): "7",
    ((0,1), (1,0)): "F",
    ((1,0), (0,1)): "F",
}


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

GREEN = '\033[92m'
RED = '\033[91m'
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


with open("example2.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    maze = Maze(lines)
    
    maze_tiles = set([])
    queue: List[Tuple[int, int]] = [(maze.start_x, maze.start_y)]
    while len(queue) > 0:
        (x, y) = queue.pop(0)
        maze_tiles.add((x, y))
        for (dx, dy) in PIPE_CONNECTIONS[maze.get(x, y)]:
            i, j = x + dx, y + dy
            if (i, j) in maze_tiles:
                continue
            queue.append((i, j))

    count = 0
    insides = set([])
    outsides = set([])
    for x in range(maze.width):
        for y in range(maze.height):
            tile = maze.get(x, y)
            if tile != ".":
                continue
            inside = reduce(operator.add, [1 for i in range(0, x) if (i, y) in maze_tiles], 0) % 2 == 1 \
                 and reduce(operator.add, [1 for i in range(x + 1, maze.width) if (i, y) in maze_tiles], 0) % 2 == 1 \
                 and reduce(operator.add, [1 for i in range(0, y) if (x, i) in maze_tiles], 0) % 2 == 1 \
                 and reduce(operator.add, [1 for i in range(y + 1, maze.height) if (x, i) in maze_tiles], 0) % 2 == 1
            if inside:
                insides.add((x, y))
                count += 1 
            else:
                outsides.add((x, y))

    print(count)
    for y in range(maze.height):
        for x in range(maze.width):
            if (x, y) in insides:
                print(GREEN + "I" + ENDC, end="")
            elif (x, y) in outsides:
                print(RED + "O" + ENDC, end="")
            else:
                print(maze.get(x, y), end="")
        print()
        



            
