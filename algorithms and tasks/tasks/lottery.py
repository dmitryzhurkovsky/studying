"""
Write a function that will return random numbers of lottery.

The lottery will draw 8 balls labeled 1 to 20.
The balls will be picked out of a bag and if the number rules below are valid we will accept
that number as a part of the lottery numbers and return the ball back in the bag. We will do
this until we get 8 lottery numbers.

Rules are:
* The same number can appear more than once
* No more than 2 occasion of duplicates are allowed

Your function should return the results sorted in ascending order.
* Examples valid draws:
    1, 2, 3, 4. 5. 6.7.8
    1, 1, 2, 2, 2, 6, 7, 8
* Example not allowed:
    1. 1. 2. 2. 3, 3,7,8
"""
import random
from collections import defaultdict

SMALLEST_NUMBER = 1
LARGEST_NUMBER = 20

COUNT_OF_BALLS = 8

MAX_COUNT_OF_ALLOWED_DUPLICATES = 2


def get_random_number(
        smallest_number: int | None = SMALLEST_NUMBER,
        largest_number: int | None = LARGEST_NUMBER
) -> int:
    return random.randint(smallest_number, largest_number)


def is_valid_draw(repeatable_numbers: set) -> bool:
    return len(repeatable_numbers) <= MAX_COUNT_OF_ALLOWED_DUPLICATES


def play() -> bool:
    """
    O(n + n + n) -> O(n)
    O(n) or O(logN). It depends on result of sorting.
    """
    draw = []

    for _ in range(COUNT_OF_BALLS + 1):  # O(n)
        number = get_random_number()
        draw.append(number)

    sorted_draw = sorted(draw)
    # O(n*logN) for average and worst cases and O(n) for te best case
    # to improve a performance(not complexity!) we can combine sorting and checking whether sentence is valid.

    count_of_repetitions_of_a_number = defaultdict(int)
    repeatable_numbers = set()
    for number in sorted_draw:  # O(n)
        count_of_repetitions_of_a_number[number] += 1

        if count_of_repetitions_of_a_number[number] >= 2:
            repeatable_numbers.add(number)

    return is_valid_draw(repeatable_numbers=repeatable_numbers)


