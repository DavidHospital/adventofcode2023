with open("input.txt", "r") as f:
    sequences = [[int(t) for t in line.split()] for line in f.readlines()]

    sum = 0
    for seq in sequences:
        diffs = [seq]
        while any([t != 0 for t in diffs[-1]]):
            curr = diffs[-1]
            diffs.append([curr[i+1] - curr[i] for i in range(len(curr) - 1)])

        for i in range(len(diffs) - 1, 0, -1):
            diffs[i-1].insert(0, diffs[i-1][0] - diffs[i][0])

        sum += diffs[0][0]
        for d in diffs:
            print(d)
        print()

    print(sum)

