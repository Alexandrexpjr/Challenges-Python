# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def get_distinct_prime_factors(number):
  factors = set() # it will save the distinct primes
  count = 2
  currentNumber = int(number) # just to assure
  while (currentNumber != 1):
    if (currentNumber % count == 0):
      factors.add(count)
      currentNumber = currentNumber / count
      continue
    count += 1
  return factors

def get_four_consecutive_integers_with_four_distinct_primes():
  numbers = list()
  curr = 2 * 3 * 5 * 7 # lowest number with 4 distinct prime factors
  while(len(numbers) < 4):
    prime_factors = get_distinct_prime_factors(curr)
    if (len(prime_factors) == 4): # if curr have 4 prime factors
      if len(numbers) == 0:
        numbers.append(curr)
        curr += 1
        continue
      if numbers[-1] == curr - 1:
        numbers.append(curr)
        curr += 1
        continue
    numbers = list()
    curr += 1
  return numbers[0]

print(get_four_consecutive_integers_with_four_distinct_primes()) # 134043

# Correct