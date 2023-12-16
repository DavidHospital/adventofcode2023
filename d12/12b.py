from typing import Any, Dict, List, Tuple
from functools import cache, reduce
import operator


SPRING = "#"
BLANK = "."
UNKNOWN = "?"

@cache
def c_check(springs: str, counts: Tuple[int, ...], curr_length) -> int:
    if len(counts) == 0:
        return 1 if springs.count(SPRING) == 0 else 0
    if len(springs) == 0:
        return 1 if len(counts) == 1 and counts[0] == curr_length else 0
    if springs[0] == BLANK:
        if curr_length == 0:
            return c_check(springs[1:], counts, 0)
        elif curr_length == counts[0]:
            return c_check(springs[1:], counts[1:], 0)
        return 0
    if springs[0] == SPRING:
        return c_check(springs[1:], counts, curr_length + 1)
    c_count = reduce(operator.add, counts, 0)
    if springs.count(SPRING) + springs.count(UNKNOWN) + curr_length < c_count:
        return 0
    return c_check(BLANK + springs[1:], counts, curr_length) \
         + c_check(SPRING + springs[1:], counts, curr_length)


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        [springs, counts] = line.split()
        counts = [int(c) for c in counts.split(",")]
        
        ex_springs = springs
        ex_counts = counts.copy()
        for i in range(4):
            ex_springs += UNKNOWN + springs
            ex_counts += counts.copy()
        
        check = c_check(ex_springs, tuple(ex_counts), 0)
        sum += check
        print(check)

    print(sum)
        
