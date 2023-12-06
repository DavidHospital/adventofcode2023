from functools import reduce
from typing import List, Tuple

almanac_map = {}
seeds = []


def range_overlap(s1: int, r1: int, s2: int, r2: int) -> Tuple[int, int]:
    start = max(s1, s2)
    rnge = min(s1 + r1, s2 + r2) - start
    return (start, rnge)


def range_diff(s1: int, r1: int, s2: int, r2: int) -> List[Tuple[int, int]]:
    result = []
    overlap = range_overlap(s1, r1, s2, r2)
    if overlap[1] <= 0:
        return [(s1, r1)]
    if overlap[0] > s1:
        result.append((s1, overlap[0] - s1))
    if s1 + r1 > overlap[0] + overlap[1]:
        result.append((overlap[0] + overlap[1], s1 + r1 - overlap[0] - overlap[1]))
    return result


def lookup(value: int, key: str = "seed", dest: str = "") -> int:
    while key != dest and key in almanac_map:
        value = next((v[0] + (value - src) for src, v in almanac_map[key].items() if src != "maps" and value >= src and value < src + v[1]), value)
        key = almanac_map[key]["maps"]
    return value


def lookup_range(start: int, rnge: int, key: str = "seed", dest: str = "") -> List[Tuple[int, int]]:
    input_ranges = [(start, rnge)]
    while key != dest and key in almanac_map:
        dest_ranges = []
        for (start, rnge) in input_ranges:
            left_overs = [(start, rnge)]
            for src, v in almanac_map[key].items():
                if src == "maps":
                    continue
                overlap = range_overlap(start, rnge, src, v[1])
                if overlap[1] > 0:
                    dest_ranges.append((overlap[0] - src + v[0], overlap[1]))
                    new_left_overs = []
                    for lo in left_overs:
                        new_left_overs += range_diff(lo[0], lo[1], overlap[0], overlap[1])
                    left_overs = new_left_overs

            dest_ranges += left_overs
        input_ranges = dest_ranges
        key = almanac_map[key]["maps"]
    return input_ranges


with open("input.txt", "r") as f:
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

ranges = []
for rnge in seed_ranges:
    ranges += lookup_range(rnge[0], rnge[1])

print(min([r[0] for r in ranges]))
