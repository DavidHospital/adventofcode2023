from functools import reduce
import operator

with open("input.txt", "r") as f:
    lines = f.readlines()
    time = int(reduce(operator.add, lines[0].split(":")[1].strip().split(), ""))
    record = int(reduce(operator.add, lines[1].split(":")[1].strip().split(), ""))

    print(f"{time}, {record}")

    sum = 0
    for i in range(0, time + 1):
        distance = (time - i) * i
        if distance > record:
            sum += 1

    print(sum)
