almanac_map = {}
seeds = []


def lookup(value: int, key: str = "seed", dest: str = "") -> int:
    while key != dest and key in almanac_map:
        value = next((v[0] + (value - src) for src, v in almanac_map[key].items() if src != "maps" and value >= src and value < src + v[1]), value)
        key = almanac_map[key]["maps"]
    return value

with open("input.txt", "r") as f:
    lines = f.readlines()

    seeds = [int(seed.strip()) for seed in lines[0].split(":")[1].split()]
    print(seeds)

    # parse almanac
    current_source = ""
    for line in lines[1:]:
        line = line.strip()

        if not line:
            continue

        if line.endswith(":"):
            # header line
            current_source = line.split("-")[0]
            current_dest = line.split("-")[2].split()[0]

            almanac_map[current_source] = {"maps": current_dest}
            
        else:
            [dest, source, rnge] = [int(p) for p in line.split()]

            almanac_map[current_source][source] = (dest, rnge)

print(min([lookup(seed) for seed in seeds]))
    
