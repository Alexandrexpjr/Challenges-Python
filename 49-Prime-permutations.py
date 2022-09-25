# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

def get_four_digit_primes():
  primes = [2, 3, 5]
  four_digit_primes = []
  for number in range(6, 10000):
    for prime in primes:
      if (number % prime == 0): break
      if (prime == primes[-1]):
        if number > 1000:
          four_digit_primes.append(number)
        primes.append(number)
  
  return four_digit_primes

def is_permutation(a, b):
  num1 = list(int(digit) for digit in str(a))
  num2 = list(int(digit) for digit in str(b))
  num1.sort(), num2.sort()
  return num1 == num2

def get_arithmetec_sequence():
  primes = get_four_digit_primes()
  perms = set()
  for a in primes:
    for b in primes:
      if (is_permutation(a, b) and a != b):
        for c in primes:
          if (is_permutation(a, c) and a != c and b != c):
            perm = [a, b, c]
            perm.sort()
            if 1487 in perm: break
            if (perm[1] - perm[0] == perm[2] - perm[1]):
              perms.update(set(x for x in perm))
          continue
        continue
      continue
  return perms


print(get_arithmetec_sequence()) #296962999629

# Correct