EMPTY = "."
GALAXY = "#"

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    expanded = [[c for c in line] for line in lines]
    width = len(lines[0])
    height = len(lines)

    # expand columns
    expand_count = 0
    for i in range(width):
        column = [line[i] for line in lines]
        if GALAXY not in column:
            for row in expanded:
                row.insert(i + expand_count, EMPTY)
            expand_count += 1

    # expand rows
    expand_count = 0
    for j in range(height):
        row = lines[j]
        if GALAXY not in row:
            expanded.insert(j + expand_count, [EMPTY for _ in range(len(expanded[0]))])
            expand_count += 1
            
    # for line in lines:
    #     print(line)
    # for row in expanded:
    #     for c in row:
    #         print(c, end="")
    #     print()

    # Find all galaxies
    galaxies = [
            (x, y) for y, line in enumerate(expanded) for x, c in enumerate(line) if c == GALAXY
            ]

    galaxy_pairs = [
            (g1, g2) for i, g1 in enumerate(galaxies) for g2 in galaxies[i+1:]
            ]

    sum = 0
    for (g1, g2) in galaxy_pairs:
        sum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    print(sum)

