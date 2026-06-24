from typing import List


def sort_words(words: List[str]) -> List[str]:
    def getWordLength(str):
        return len(str)
    words.sort(key=getWordLength, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    def getAbs(num):
        return abs(num)
    
    numbers.sort(key=getAbs)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
