# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

def rotate_digits(n):
  rotations = [n]
  digits_list = list(str(n))
  while (len(rotations) < len(str(n))):
    digits_list.append(digits_list[0])
    digits_list.pop(0)
    rotations.append(int(''.join(digits_list)))
  return set(rotations)

def get_all_primes_below_n(n):
  primes = [2, 3]
  for number in range(3, n, 2):
    for prime in primes:
      if(number % prime == 0):
        break
      if(prime == primes[-1]): 
        primes.append(number)
  return primes

def circular_primes_below_n(n):
  all_primes = get_all_primes_below_n(n)
  count = 1
  for prime in all_primes:
    if(any(int(digit) % 2 == 0 for digit in list(str(prime)))): continue
    if (all(rotation in all_primes for rotation in (rotate_digits(prime)))):
      count += 1
  return count

print(circular_primes_below_n(1000000)) # 55

# Correct, but takes 7 min. (i'll try to refactor) 