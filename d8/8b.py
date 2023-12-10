import math

with open("input.txt", "r") as f:
    lines = f.readlines()

    instructions = lines[0].strip()

    nodes = {}
    starts = []
    for line in lines[2:]:
        parts = line.strip().split("=")
        key = parts[0].strip()
        dirs = parts[1].strip()[1:-1].split(",")
        nodes[key] = (dirs[0].strip(), dirs[1].strip())
        if key.endswith("A"):
            starts.append(key)


    counter = 0
    end_times = [0 for _ in range(len(starts))]
    while any([e == 0 for e in end_times]):
        instruction = instructions[counter % len(instructions)]
        counter += 1
        for idx, start in enumerate(starts):
            if end_times[idx] > 0:
                continue
            starts[idx] = nodes[start][0 if instruction == "L" else 1]
            if starts[idx].endswith("Z"):
                end_times[idx] = counter
    
    print(math.lcm(*end_times))
