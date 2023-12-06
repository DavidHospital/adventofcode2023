from functools import reduce
from typing import List, Tuple

almanac_map = {}
seeds = []


def range_overlap(s1: int, r1: int, s2: int, r2: int) -> Tuple[int, int]:
    start = max(s1, s2)
    rnge = min(s1 + r1, s2 + r2) - start
    return (start, rnge)


def lookup(value: int, key: str = "seed", dest: str = "") -> int:
    while key != dest and key in almanac_map:
        value = next((v[0] + (value - src) for src, v in almanac_map[key].items() if src != "maps" and value >= src and value < src + v[1]), value)
        key = almanac_map[key]["maps"]
    return value


def lookup_range(start: int, rnge: int, key: str = "seed", dest: str = "") -> List[Tuple[int, int]]:
    dest_ranges = []
    for src, v in almanac_map[key].items():
        if src == "maps":
            continue
        overlap = range_overlap(start, rnge, src, v[1])
        if overlap[1] > 0:
            dest_ranges.append(overlap)
    return []


with open("example.txt", "r") as f:
    lines = f.readlines()

    seeds = [int(seed.strip()) for seed in lines[0].split(":")[1].split()]
    # print(seeds)

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

# print(min([lookup(seed) for seed in seeds]))

it = iter(seeds)
seed_ranges = [(x, next(it)) for x in it]
# print(seed_ranges)

for rnge in seed_ranges:
    print(lookup_range(rnge[0], rnge[1]))
    
