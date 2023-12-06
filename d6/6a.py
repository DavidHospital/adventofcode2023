

with open("input.txt", "r") as f:
    lines = f.readlines()
    times = [int(n) for n in lines[0].split(":")[1].strip().split()]
    distances = [int(n) for n in lines[1].split(":")[1].strip().split()]

    product = 1
    for time, record in zip(times, distances):
        print(f"{time}, {record}")

        sum = 0
        for i in range(0, time + 1):
            distance = (time - i) * i
            if distance > record:
                sum += 1
        product *= sum
    print(product)
