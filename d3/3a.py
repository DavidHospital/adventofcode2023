from typing import List


EMPTY_CHAR = "."
REDC = '\033[91m'
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

    def check_coord(self, x: int, y: int) -> bool:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.is_symbol(i, j):
                    return True
        return False


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    schematic = Schematic(lines)

    part_sum = 0
    current_num = ""
    current_indices = []
    for j, line in enumerate(schematic.lines):
        for idx, char in enumerate(line):
            if char.isnumeric():
                current_num += char
                current_indices.append(idx)
            elif current_num:
                nearby_symbol = False
                for i in current_indices:
                    nearby_symbol = nearby_symbol or schematic.check_coord(i, j)
                if nearby_symbol:
                    part_sum += int(current_num)
                    print(REDC + current_num + ENDC, end="")
                else:
                    print(current_num, end="")
                print(char, end="")
                current_num = ""
                current_indices = []
            else:
                print(char, end="")
        if current_num:
            nearby_symbol = False
            for i in current_indices:
                nearby_symbol = nearby_symbol or schematic.check_coord(i, j)
            if nearby_symbol:
                part_sum += int(current_num)
                print(REDC + current_num + ENDC, end="")
            else:
                print(current_num, end="")
            current_num = ""
            current_indices = []
        print()
    print(part_sum)





