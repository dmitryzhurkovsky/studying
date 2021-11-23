from typing import Optional


def binary_search(sorted_list: list, item: int) -> Optional[int]:
    """O(logN)"""
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


test = [0, 2, 4, 6, 8, 10, 12, 15, 17]
print(binary_search(test, 4))
