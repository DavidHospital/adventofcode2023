import operator
from functools import reduce

with open("input.txt", "r") as f:
    lines = f.readlines()
    card_count = {i: 1 for i in range(1, len(lines) + 1)}
    for line in lines:
        parts = line.strip().split("|")
        game_id = int(parts[0].split(":")[0].strip().split()[1])
        winning_numbers = set([int(n) for n in parts[0].split(":")[1].strip().split()])
        your_numbers = [int(n) for n in parts[1].strip().split()]

        winnings = len(winning_numbers.intersection(your_numbers))
        for i in range(1, winnings + 1):
            if game_id + i in card_count:
                card_count[game_id + i] += card_count[game_id]
    print(reduce(operator.add, card_count.values()))







