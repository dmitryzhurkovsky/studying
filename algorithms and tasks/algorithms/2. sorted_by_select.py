def find_smallest(array: list) -> int:
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array: list) -> list:
    """O(n*n)"""
    new_arr = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_arr.append(array.pop(smallest))
    return new_arr
