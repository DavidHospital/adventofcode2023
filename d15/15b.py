from functools import reduce
from typing import List


class Box:
    def __init__(self, id: int) -> None:
        self.id = id
        self.lenses = {}
        self.size = 0

    def add_lense(self, label: str, focal: int) -> None:
        if label not in self.lenses:
            self.lenses[label] = (self.size, focal)
            self.size += 1
        else:
            self.lenses[label] = (self.lenses[label][0], focal)

    def rm_lense(self, label: str) -> None:
        if label not in self.lenses:
            return
        del self.lenses[label]

    def is_empty(self) -> bool:
        return len(self.lenses) == 0

    def ordered_lenses(self) -> List[str]:
        sorted_keys = sorted(self.lenses, key=self.lenses.get)
        return [(key, self.lenses[key][1]) for key in sorted_keys]

def hash(string: str) -> int:
    return reduce(lambda r, c: (r + ord(c)) * 17 % 256, string, 0)

with open("input.txt", "r") as f:
    instructions = f.readline().strip().split(",")
    print(instructions)

    boxes = [Box(i) for i in range(256)]

    for instr in instructions:
        if '=' in instr:
            parts = instr.split("=")
            boxes[hash(parts[0])].add_lense(parts[0], int(parts[1]))
        elif '-' in instr:
            label = instr.split("-")[0]
            boxes[hash(label)].rm_lense(label)

    sum = 0
    for box in boxes:
        if not box.is_empty():
            print(box.id)
            print(box.ordered_lenses())

            for idx, lense in enumerate(box.ordered_lenses()):
                sum += (box.id + 1) * (idx + 1) * lense[1]

    print(sum)
