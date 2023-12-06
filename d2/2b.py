from functools import reduce
import operator

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        parts = line.split(":")
        game_idx = parts[0].split(" ")[1]
        rounds = parts[1].strip().split(";")

        min_colors = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        for round in rounds:
            picks = round.strip().split(",")
            for pick in picks:
                [num, color] = pick.strip().split(" ")
                min_colors[color] = max(int(num), min_colors[color])
        power = reduce(operator.mul, min_colors.values(), 1)
        print(f"Game {game_idx}: {power}")
        sum += power
    print(sum)

