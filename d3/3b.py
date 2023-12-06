from typing import List, Tuple


EMPTY_CHAR = "."
GEAR_CHAR = "*"

REDC = '\033[91m'
GREENC = '\033[92m'
ENDC = '\033[0m'


class Schematic:
    def __init__(self, lines: List[str]) -> None:
        self.lines = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def is_symbol(self, x: int, y: int) -> bool:
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return False
        char = self.lines[y][x]
        return not char.isnumeric() and char != EMPTY_CHAR

    def is_gear(self, x: int, y: int) -> bool:
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return False
        return self.lines[y][x] == GEAR_CHAR

    def check_coord(self, x: int, y: int) -> bool:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.is_symbol(i, j):
                    return True
        return False

    def find_gears(self, x: int, y: int) -> List[Tuple[int, int]]:
        gears = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.is_gear(i, j):
                    gears.append((i, j))
        return gears


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    schematic = Schematic(lines)

    gear_sum = 0
    current_num = ""
    current_indices = []

    gears_map = {}
    for j, line in enumerate(schematic.lines):
        for idx, char in enumerate(line):
            if char.isnumeric():
                current_num += char
                current_indices.append(idx)
            elif current_num:
                gears_lst = []
                for i in current_indices:
                    gears_lst += schematic.find_gears(i, j)
                gears = set(gears_lst)
                for gear in gears:
                    if gear not in gears_map:
                        gears_map[gear] = []
                    gears_map[gear].append(int(current_num))
                current_num = ""
                current_indices = []
        if current_num:
            gears_lst = []
            for i in current_indices:
                gears_lst += schematic.find_gears(i, j)
            gears = set(gears_lst)
            for gear in gears:
                if gear not in gears_map:
                    gears_map[gear] = []
                gears_map[gear].append(int(current_num))
            current_num = ""
            current_indices = []
    for j, line in enumerate(schematic.lines):
        for idx, char in enumerate(line):
            if char == GEAR_CHAR:
                gear_nums = gears_map.get((idx, j), [])
                if len(gear_nums) == 2:
                    gear_sum += gear_nums[0] * gear_nums[1]
                    print(GREENC + char + ENDC, end="")
                else:
                    print(REDC + char + ENDC, end="")
            else:
                print(char, end="")
        print()
    print(gear_sum)

