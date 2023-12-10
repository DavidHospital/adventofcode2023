from __future__ import annotations

from enum import Enum
from functools import cmp_to_key, reduce
import operator


CARDS = {
    "J": -1,
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "Q": 10,
    "K": 11,
    "A": 12,
}


class HandType(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Hand:
    def __init__(self, cards: str, bet: int):
        assert len(cards) == 5
        self.cards = cards
        self.bet = bet
    
    def calculate(self) -> HandType:
        card_counts = {}
        j_count = 0
        for c in self.cards:
            if c == "J":
                j_count += 1
                continue
            if c not in card_counts:
                card_counts[c] = 0
            card_counts[c] += 1
        max_count = max(card_counts.values(), default=0) + j_count
        if max_count == 5:
            return HandType.FIVE_OF_A_KIND
        elif max_count == 4:
            return HandType.FOUR_OF_A_KIND
        elif max_count == 3:
            return HandType.FULL_HOUSE if len(card_counts) == 2 else HandType.THREE_OF_A_KIND
        elif max_count == 2:
            return HandType.TWO_PAIR if len(card_counts) == 3 else HandType.PAIR
        else:
            return HandType.HIGH_CARD

    def __repr__(self):
        return f"({self.cards}, {self.bet})"

    @staticmethod
    def compare(a: Hand, b: Hand) -> int:
        a_calc = a.calculate()
        b_calc = b.calculate()

        if a_calc == b_calc:
            for ac, bc in zip(a.cards, b.cards):
                if ac == bc: continue
                return -1 if CARDS[ac] < CARDS[bc] else 1
        return -1 if a_calc.value < b_calc.value else 1


with open("input.txt", "r") as f:
    lines = f.readlines()

    splits = [line.split() for line in lines]
    hands = [Hand(cards, int(bet)) for [cards, bet] in splits]

    sorted_hands = sorted(hands, key=cmp_to_key(Hand.compare))

    print(sorted_hands)
   
    sum = reduce(operator.add, [(idx + 1) * hand.bet for idx, hand in enumerate(sorted_hands)])
    
    print(sum)

