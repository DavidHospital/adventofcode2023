from typing import Any, Dict, List, Tuple
from functools import reduce
import operator


SPRING = "#"
BLANK = "."
UNKNOWN = "?"


# c_map: Dict[Tuple[str, List[int]], int] = {}
def log_ret(ret: Any) -> Any:
    # print(ret)
    return ret


def c_check(springs: str, counts: List[int]) -> int:
    # if (springs, counts) in c_map:
    #     return c_map[(springs, counts)]
    # print(springs, counts)
    s_count = springs.count(SPRING)
    u_count = springs.count(UNKNOWN)
    if reduce(operator.add, counts, 0) > s_count + u_count:
        return log_ret(0)
    count_idx = 0
    prev = None
    for idx, s in enumerate(springs):
        if count_idx >= len(counts):
            if springs[idx:].count(SPRING) == 0:
                return log_ret(1)
            return log_ret(0)
        if s == BLANK:
            if counts[count_idx] == 0:
                count_idx += 1
            elif prev == SPRING:
                return log_ret(0)
        elif s == SPRING:
            counts[count_idx] -= 1
            if counts[count_idx] < 0:
                return log_ret(0)
        elif s == UNKNOWN:
            if counts[count_idx] == 0 and prev == SPRING:
                return log_ret(c_check(BLANK + springs[idx+1:], counts[count_idx:]))
            if counts[count_idx] > 0 and prev == SPRING:
                return log_ret(c_check(SPRING + springs[idx+1:], counts[count_idx:]))
            return log_ret(c_check(BLANK + springs[idx+1:], counts[count_idx:].copy()) + c_check(SPRING + springs[idx+1:], counts[count_idx:].copy()))
        prev = s

    return log_ret(1) if reduce(operator.add, counts[count_idx:], 0) == 0 else log_ret(0)


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        [springs, counts] = line.split()
        counts = [int(c) for c in counts.split(",")]
        
        print(springs, counts)
        check = c_check(springs, counts)
        sum += check
        print(check)
    print(sum)
        
