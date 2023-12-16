

def flip(c):
    return "#" if c == "." else "."

def fixed_puzzles(puzzle):
    for r, line in enumerate(puzzle):
        for c, char in enumerate(line):
            fixed = puzzle.copy()
            fixed[r] = line[:c] + flip(char) + line[c+1:]
            yield fixed

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
        for l in puzzle:
            print(l)
        print()
        orig = None

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
            orig = f"h{line}"

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
            orig = f"v{line}"

        print(orig)
        for fixed in fixed_puzzles(puzzle):

            # check horizontal reflections
            line = -1
            for i in range(1, len(fixed)):
                good = True
                for k in range(min(i, len(fixed) - i)):
                    if fixed[i - k - 1] != fixed[i + k]:
                        good = False
                if good and f"h{i}" != orig:
                    line = i
                    break
            if line != -1:
                sum += 100 * line
                break

            # check vertical reflections
            line = -1
            for i in range(1, len(fixed[0])):
                good = True
                for k in range(min(i, len(fixed[0]) - i)):
                    if [line[i - k - 1] for line in fixed] != [line[i + k] for line in fixed]:
                        good = False
                if good and f"v{i}" != orig:
                    line = i
                    break
            if line != -1:
                sum += line
                break


    print(sum)
