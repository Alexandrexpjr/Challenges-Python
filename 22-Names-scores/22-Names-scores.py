import os

os.chdir('./22-Names-scores/')

f = open("p022_names.txt", "r")

all_names = f.read()

all_names = all_names.split(',')
all_names.sort()

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

def get_name_value(name):
  sum = 0
  for letter in name:
    if(letter == '"'): pass
    sum += letter_enum[letter]
  return sum

get_name_value(all_names[0]) # worked

def get_score(name, index):
  return get_name_value(name) * (index + 1)

get_score('"ABEL"', 6)

def all_names_score(names_list):
  score = 0
  for index in range(len(names_list)):
    score += get_score(names_list[index], index)
  return score

print(all_names_score(all_names)) # 871198282

# Correct