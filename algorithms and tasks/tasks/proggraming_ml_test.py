from collections import defaultdict


def solution(input_data: list[int]) -> int:
    max_number = -10000
    for number in input_data:
        if number > max_number and number % 3 == 0:
            max_number = number

    return max_number


def solution2(input_data: str) -> bool:
    first_letter = input_data[0]
    letter_b_met = False

    for letter in input_data[1:]:
        if first_letter == 'b' and letter == 'a':
            return False

        if letter == 'b' and not letter_b_met:
            letter_b_met = True

        if letter == 'a' and letter_b_met:
            return False

    return True


def solution(input_data: str) -> int:
    tmp_letter = input_data[0]
    count_of_letters = defaultdict(int)
    block_number = 1

    for letter in input_data:
        if letter != tmp_letter:
            block_number += 1
        count_of_letters[block_number] += 1
        tmp_letter = letter

    count_of_letters = sorted(count_of_letters.items(), key=lambda x: x[1], reverse=True)

    max_count_of_letters_in_one_block = count_of_letters[0][1]

    result = 0
    for block, count_of_letters in count_of_letters[1:]:
        result += max_count_of_letters_in_one_block - count_of_letters

    return result
