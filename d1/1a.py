with open("input.txt", "r") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        first = next((int(c) for c in line if c.isnumeric()), 0) 
        last = next((int(c) for c in line[::-1] if c.isnumeric()), 0)
        print(f"first: {first}, last: {last}")
        sum += int(f"{first}{last}")
    print(sum)
