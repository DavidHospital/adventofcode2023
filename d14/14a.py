with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    width = len(lines[0])
    height = len(lines)

    for line in lines:
        print(line)

    # tilt platform up
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

    print()
    sum = 0
    for row, line in enumerate(lines):
        print(line)
        sum += line.count("O") * (height - row)

    print(sum)

