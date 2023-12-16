REDC = '\033[91m'

def spin_cycle(lines): 
    lines = lines.copy()

    width = len(lines[0])
    height = len(lines)

    # tilt platform N
    for col in range(width):
        barrier = -1

        for row in range(height):
            char = lines[row][col]

            if char == ".":
                continue
            if char == "#":
                barrier = row
            elif char == "O":
                barrier += 1
                lines[barrier] = lines[barrier][:col] + "O" + lines[barrier][col+1:]
                if barrier != row:
                    lines[row] = lines[row][:col] + "." + lines[row][col+1:]
    # tilt platform W
    for row in range(height):
        barrier = -1

        for col in range(width):
            char = lines[row][col]

            if char == ".":
                continue
            if char == "#":
                barrier = col
            elif char == "O":
                barrier += 1
                lines[row] = lines[row][:barrier] + "O" + lines[row][barrier+1:]
                if barrier != col:
                    lines[row] = lines[row][:col] + "." + lines[row][col+1:]
    # tilt platform S
    for col in range(width):
        barrier = height

        for row in range(height-1,-1,-1):
            char = lines[row][col]

            if char == ".":
                continue
            if char == "#":
                barrier = row
            elif char == "O":
                barrier -= 1
                lines[barrier] = lines[barrier][:col] + "O" + lines[barrier][col+1:]
                if barrier != row:
                    lines[row] = lines[row][:col] + "." + lines[row][col+1:]
    # tilt platform W
    for row in range(height):
        barrier = width

        for col in range(width-1,-1,-1):
            char = lines[row][col]

            if char == ".":
                continue
            if char == "#":
                barrier = col
            elif char == "O":
                barrier -= 1
                lines[row] = lines[row][:barrier] + "O" + lines[row][barrier+1:]
                if barrier != col:
                    lines[row] = lines[row][:col] + "." + lines[row][col+1:]

    return lines


def calc_load(state):
    height = len(state)
    sum = 0
    for row, line in enumerate(state):
        print(line)
        sum += line.count("O") * (height - row)
    return sum


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    prev = []
    while lines not in prev:
        prev.append(lines.copy())
        lines = spin_cycle(lines)

    cycle_len = len(prev) - next(idx for idx, p in enumerate(prev) if p == lines)
    full_cycle = prev[len(prev)-cycle_len:]
    # for snapshot in full_cycle:
    #     for line in snapshot:
    #         print(line)
    #     print()
    # for line in lines:
    #     print(line)
    print(len(full_cycle))

    final_state = full_cycle[(1_000_000_000 - len(prev)) % len(full_cycle)]
    for line in final_state:
        print(line)
    
    print(calc_load(final_state))
    
