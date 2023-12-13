EMPTY = "."
GALAXY = "#"

EXPANSION_FACTOR = 1000000

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    width = len(lines[0])
    height = len(lines)

    # expand columns
    ex_rows = set()
    ex_cols = set()

    for i in range(width):
        column = [line[i] for line in lines]
        if GALAXY not in column:
            ex_cols.add(i)

    # expand rows
    for j in range(height):
        row = lines[j]
        if GALAXY not in row:
            ex_rows.add(j)
            
    # Find all galaxies
    galaxies = [
            (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == GALAXY
            ]

    galaxy_pairs = [
            (g1, g2) for i, g1 in enumerate(galaxies) for g2 in galaxies[i+1:]
            ]

    sum = 0
    for (g1, g2) in galaxy_pairs:
        dist = 0
        x_diff = abs(g1[0] - g2[0])
        y_diff = abs(g1[1] - g2[1])
        dist += x_diff
        dist += y_diff
        for i in range(1, x_diff):
            if min(g1[0], g2[0]) + i in ex_cols:
                dist += EXPANSION_FACTOR - 1
        for j in range(1, y_diff):
            if min(g1[1], g2[1]) + j in ex_rows:
                dist += EXPANSION_FACTOR - 1
        sum += dist
    print(sum)

