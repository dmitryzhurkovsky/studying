def quick_sort(array: list) -> list:
    """O(n*n). Isn't greedy algorithm"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # pivot - точка опоры, опорный элемент
        less = [i for i in array[1:] if i <= pivot]
        grater = [i for i in array[1:] if i >= pivot]

        return quick_sort(less) + [pivot] + quick_sort(grater)
