# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import os

os.chdir('./42-Coded-triangle-numbers/')
file = open('p042_words.txt', 'r')
words = file.read()

letter_enum = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
    '"': 0
}

def get_pontuation(word):
    pontuation = 0
    for letter in word:
        pontuation += letter_enum[letter]
    return pontuation

def transform_file_in_list(file):
    file_list = file.split(',')
    return file_list

def get_list_pontuation():
    word_list = transform_file_in_list(words)
    pontuations = []
    for word in word_list:
        pontuations.append(get_pontuation(word))
    return pontuations

print(max(get_list_pontuation())) # The biggest pontuation is 192, so i only have to get the triangle numbers below 192

def get_triangle_numbers_sequence_below_n(n):
    sequence = [1]
    count = 2
    while(sequence[-1] < n):
        curr =  (count * 0.5) * (count + 1)
        sequence.append(curr)
        count += 1
    return sequence

def words_pontuation_inside_file():
    count = 0
    list_of_pontuations = get_list_pontuation()
    triangle_sequence = get_triangle_numbers_sequence_below_n(max(list_of_pontuations))
    for pontuation in list_of_pontuations:
        if pontuation in triangle_sequence:
            count += 1
    return count

print(words_pontuation_inside_file()) # 162

# Correct