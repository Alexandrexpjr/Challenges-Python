# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes four parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
# 4. List to be filled
def permute(string, initial_index, last_index, perms):
  if initial_index == last_index:
    perms.append(toString(string))
  else:
    for i in range(initial_index,last_index+1):
      string[initial_index], string[i] = string[i], string[initial_index]
      permute(a, initial_index+1, last_index, perms)
      string[initial_index], string[i] = string[i], string[initial_index] # backtrack

def get_perms(a, n):
  perms = []
  permute(a, 0, n-1, perms)
  return perms

def sortPerms(perms):
  ordened_perms = []
  for number in perms:
    ordened_perms.append(int(number))
  ordened_perms.sort()
  return ordened_perms

def get_nth_perm(perms, n):
  return perms[n-1]

string = "0123456789"
n = len(string)
a = list(string)

permutations = get_perms(a, n)
sorted = sortPerms(permutations)
print(get_nth_perm(sorted, 1000000)) # 2783915460

# Correct

# Code inspired by geekforgeeks, link: https://www.geeksforgeeks.org/lexicographic-permutations-of-string/