# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def get_n_primes(n):
  primes = [2, 3, 5]
  current = 5
  while(len(primes) < n):
    for number in primes:
      if (current % number == 0):
        break
      if (number > primes[-1] ** 0.5):
        primes.append(current)
        break
    current += 1
  return primes

import math
def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

def get_smallest_odd_composite_number(initial_size):
  primes = get_n_primes(initial_size)
  current = 9
  smallest = 0
  while (smallest == 0):
    if current in primes:
      current += 2
      continue
    for prime in primes:
      if (prime > current):
        smallest = current
        break
      curr_sqr = (current - prime) / 2

      if (is_square(curr_sqr)):
        break
      continue
    current += 2
  return smallest

print(get_smallest_odd_composite_number(1000)) # 5777

# Correct