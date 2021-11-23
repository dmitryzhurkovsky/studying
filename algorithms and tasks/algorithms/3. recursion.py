"""Pseudocode"""
"""
1. Cycle
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()  # pile - куча
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('Key has been found!')
                
2. Recursion
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look)for_key(item)
        elif item.is_a_key():
            print('Key has been found!')
"""


def countdown(i: int) -> None:
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


def factorial(x: int) -> int:
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


def find_number_sum(sequence: list) -> int:
    if len(sequence) == 0:
        return 0
    else:
        return sequence[0] + find_number_sum(sequence[1:])


def find_number_count(sequence: list) -> int:
    if len(sequence) == 0:
        return 0
    else:
        return 1 + find_number_count(sequence[1:])


def find_max_number(sequence: list) -> int:
    if len(sequence) == 2:
        return sequence[0] if sequence[0] > sequence[1] else sequence[1]
    else:
        sub_max = find_max_number(sequence[1:])

        return sequence[0] if sequence[0] > sub_max else sub_max


"""Fibonacci numbers"""
# By Recursion
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1


# By Cycle
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


# By generator
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# By generator, infinity
def fib() -> int:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
