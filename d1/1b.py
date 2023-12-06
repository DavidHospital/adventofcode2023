numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def get_first_last_numbers(word, index=0):
    word = word.lower()
    first = last = None
    for i in range(len(word)):
        if first is not None:
            break
        if word[i].isnumeric():
            first = int(word[i])
            break
        for key in numbers.keys():
            if word[i:].startswith(key):
                first = numbers[key]
                break
        
    for i in range(len(word) - 1, -1, -1):
        if last is not None:
            break
        if word[i].isnumeric():
            last = int(word[i])
            break
        for key in numbers.keys():
            if word[i:].startswith(key):
                last = numbers[key]
                break
    if first is None:
        raise Exception(f"index: {index}, First number not found")
    if last is None:
        raise Exception(f"index: {index}, Last number not found")
    return first or 0, last or 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for idx, line in enumerate(lines):
        first, last = get_first_last_numbers(line, idx)
        print(f"{first}{last}")
        sum += int(f"{first}{last}")
    print(sum)
