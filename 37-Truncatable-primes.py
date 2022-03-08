# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def get_truncatable_numbers(n):
  numbers = []
  for i in range(1, len(str(n))):
    numbers.extend((int(str(n)[i:]), int(str(n)[:i])))
  return numbers

def get_all_primes_below_n(n):
  primes = [2, 3]
  for number in range(3, n, 2):
    for prime in primes:
      if(number % prime == 0):
        break
      if(prime == primes[-1]): 
        primes.append(number)
  return primes

def sum_of_eleven_primes_truncatables():
  truncatables = []
  primes = get_all_primes_below_n(750000) # I try first 10.000 and increase the value till i get eleven truncatable primes
  for prime in primes:
    if (len(truncatables) == 11): break
    if (prime < 10): continue
    if(all(n in primes for n in get_truncatable_numbers(prime))):
      truncatables.append(prime)
  print(truncatables)
  return sum(truncatables) # 748317

print(sum_of_eleven_primes_truncatables())

# Correct