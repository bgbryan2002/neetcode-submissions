from typing import List

def get_word_length(word:str)-> int:
    return len(word)   

def sort_words(words: List[str]) -> List[str]:
    words.sort(key = get_word_length, reverse = True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    m = []
    i = 0
    while i < len(numbers) in numbers:
        m.append(numbers[i])
    m.sort()
    return m

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
