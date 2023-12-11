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
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbour = self.get(x + dx, y + dy)
                if neighbour in PIPE_CONNECTIONS and any(dx + di == 0 and dy + dj == 0 for (di, dj) in PIPE_CONNECTIONS[neighbour]):
                    neighbours.append((dx, dy))
            assert len(neighbours) == 2
            return CONNECTION_PIPES[(neighbours[0], neighbours[1])]
        return self.lines[y][x]


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    maze = Maze(lines)
    
    completed = {}
    queue: List[Tuple[int, int, int]] = [(maze.start_x, maze.start_y, 0)]
    highest = 0
    while len(queue) > 0:
        (x, y, dist) = queue.pop(0)
        completed[(x, y)] = dist
        for (dx, dy) in PIPE_CONNECTIONS[maze.get(x, y)]:
            i, j = x + dx, y + dy
            if (i, j) in completed:
                continue
            queue.append((i, j, dist + 1))

    print(max(v for v in completed.values())) 
        

