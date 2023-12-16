
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    puzzles = []

    start = 0
    for idx, line in enumerate(lines):
        if not line:
            puzzles.append(lines[start:idx])
            start = idx + 1

    sum = 0
    for puzzle in puzzles:
        # check horizontal reflections
        line = -1
        for i in range(1, len(puzzle)):
            good = True
            for k in range(min(i, len(puzzle) - i)):
                if puzzle[i - k - 1] != puzzle[i + k]:
                    good = False
            if good:
                line = i
                break
        if line != -1:
            sum += 100 * line
            continue

        # check vertical reflections
        line = -1
        for i in range(1, len(puzzle[0])):
            good = True
            for k in range(min(i, len(puzzle[0]) - i)):
                if [line[i - k - 1] for line in puzzle] != [line[i + k] for line in puzzle]:
                    good = False
            if good:
                line = i
                break
        if line != -1:
            sum += line
            continue

    print(sum)
