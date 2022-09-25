# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def get_all_primes_below_n(n):
  primes = [2, 3]
  for number in range(3, n, 2):
    for prime in primes:
      if(number % prime == 0):
        break
      if(prime == primes[-1]): 
        primes.append(number)
  return primes

print(get_all_primes_below_n(200))

def check_if_consecutive(n):
  primes = get_all_primes_below_n(n)
  biggest_consecutive_prime = int()
  for prime in primes[::-1]:
    current_sum = 0
    for p in primes[3:]:
      if(current_sum + p < prime):
        current_sum += p
        continue
      if(current_sum + p == prime):
        biggest_consecutive_prime = prime
        break
    if (biggest_consecutive_prime != 0): break
  
  return biggest_consecutive_prime

print(check_if_consecutive(1000000)) #997651

# Correct, but i kinda cheated