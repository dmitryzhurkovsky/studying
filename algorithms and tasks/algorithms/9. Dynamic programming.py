"""Find the longest common subsequence between two words"""
from typing import Union
# import numpy as np


test_dictionary = ['fish', 'fose']

input_misspelled_word = 'fosha'


def find__common_subsequence(
        dictionary: list,
        misspelled_word: str,
        count_of_supposed_words: int = 5
) -> Union[list, str, None]:
    supposed_words = dict()
    subsequences_of_identical_length = 0

    correct_word = None
    identical_letters = 0

    for word_from_dictionary in dictionary:
        cell = [[0 for _ in misspelled_word] for _ in word_from_dictionary]
        # cell = np.zeros((len(word_from_dictionary), len(misspelled_word)))

        tmp_identical_letters = 0
        for y in range(len(word_from_dictionary)):
            for x in range(len(misspelled_word)):
                if word_from_dictionary[y] == misspelled_word[x]:
                    cell[y][x] = cell[y - 1][x - 1] + 1
                    tmp_identical_letters += 1
                else:
                    cell[y][x] = max(cell[y - 1][x], cell[y][x - 1])

        if tmp_identical_letters > identical_letters:
            correct_word = word_from_dictionary
            supposed_words[word_from_dictionary] = tmp_identical_letters

        elif identical_letters == tmp_identical_letters:
            supposed_words[word_from_dictionary] = tmp_identical_letters
            subsequences_of_identical_length += 1

        identical_letters = tmp_identical_letters

    if subsequences_of_identical_length > 0:
        return sorted(supposed_words, key=lambda item: item[1], reverse=True)[:count_of_supposed_words]

    return correct_word


if __name__ == '__main__':
    result = find__common_subsequence(dictionary=test_dictionary, misspelled_word=input_misspelled_word)
    print(result)