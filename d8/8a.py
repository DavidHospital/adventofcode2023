START_NODE = "AAA"
END_NODE = "ZZZ"

with open("input.txt", "r") as f:
    lines = f.readlines()

    instructions = lines[0].strip()

    nodes = {}
    start = START_NODE
    for line in lines[2:]:
        parts = line.strip().split("=")
        key = parts[0].strip()
        dirs = parts[1].strip()[1:-1].split(",")
        nodes[key] = (dirs[0].strip(), dirs[1].strip())


    counter = 0
    while start != END_NODE:
        instruction = instructions[counter % len(instructions)]
        start = nodes[start][0 if instruction == "L" else 1]
        counter += 1
        print(f"{instruction}, {start}")
    
    print(counter)

