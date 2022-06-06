# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

primes = [2, 3, 5, 7, 11, 13, 17]

def permute(current_perm, initial_index, last_index, perms):
    if (initial_index==last_index):
        perms.append(tuple(current_perm))
    else:
        for i in range(initial_index,last_index+1):
            current_perm[initial_index], current_perm[i] = current_perm[i], current_perm[initial_index]
            permute(current_perm, initial_index+1, last_index, perms)
            current_perm[initial_index], current_perm[i] = current_perm[i], current_perm[initial_index] # backtrack

def get_permutations(initial_perm):
  perms = []
  permute(list(initial_perm), 0, len(initial_perm) - 1, perms)
  return perms

def get_0_to_9_pandigital():
  return get_permutations('0123456789')

def get_pandigital_with_property():
  pandigitals = get_0_to_9_pandigital()
  numbers = []
  for pandigital in pandigitals:
    for index in range(1, 8):
      substring = pandigital[index:index + 3]
      subnumber = str()
      for sub in substring:
        subnumber += sub
      if (int(subnumber) % primes[index - 1] != 0):
        break
      if (index == 7):
        pandigital_str = str()
        for digit in pandigital:
          pandigital_str += digit
        numbers.append(int(pandigital_str))
  return sum(numbers)

print(get_pandigital_with_property()) # 16695334890

# Correct