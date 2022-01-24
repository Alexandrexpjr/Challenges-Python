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
def permute(a, l, r, f):
    if l==r:
        f.append(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, f)
            a[l], a[i] = a[i], a[l] # backtrack

def teste(a, n):
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

permutations = teste(a, n)
sorted = sortPerms(permutations)
print(get_nth_perm(sorted, 1000000)) # 2783915460

# Correct

# Code inspired by geekforgeeks, link: https://www.geeksforgeeks.org/lexicographic-permutations-of-string/