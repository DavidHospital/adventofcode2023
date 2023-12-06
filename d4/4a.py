

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        parts = line.strip().split("|")
        winning_numbers = set([int(n) for n in parts[0].split(":")[1].strip().split()])
        your_numbers = [int(n) for n in parts[1].strip().split()]

        points = 0
        for num in your_numbers:
            if num in winning_numbers:
                points = points * 2 or 1
        sum += points
    print(sum)




