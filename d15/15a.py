from functools import reduce

def hash(string: str) -> int:
    return reduce(lambda r, c: (r + ord(c)) * 17 % 256, string, 0)

with open("input.txt", "r") as f:
    instructions = f.readline().strip().split(",")
    print(instructions)

    sum = 0
    for instr in instructions:
        sum += hash(instr)
    print(sum)
