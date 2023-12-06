

COLOR_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        parts = line.split(":")
        game_idx = parts[0].split(" ")[1]
        rounds = parts[1].strip().split(";")
        valid_game = True
        for round in rounds:
            picks = round.strip().split(",")
            for pick in picks:
                [num, color] = pick.strip().split(" ")
                if COLOR_LIMITS[color] < int(num):
                    valid_game = False
        print(f"Game {game_idx}: {valid_game}")
        sum += int(game_idx) if valid_game else 0
    print(sum)

