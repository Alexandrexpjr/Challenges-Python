# 27 - Quadratic Primes 
# Explanation: https://projecteuler.net/problem=27

# n² + an + b

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

def get_quadratic_expression(a, b, n):
  return (n**2 + a*n + b)

def get_n_primes(n):
  primes = [2, 3, 5]
  current = 5
  while(len(primes) < n):
    for number in primes:
      if (current % number == 0):
        break
      if (number == primes[-1]): primes.append(current)
    current += 1
  return primes

ten_thousand_primes = get_n_primes(10000)

def get_optimal_expression_ab_product():
  optimal_a = 0
  optimal_b = 0
  current_n = 0
  for a in range(-1000, 1000):
    for b in range(-1000, 1000):
      number_of_primes = 0
      n = 0
      while(get_quadratic_expression(a, b, n) in ten_thousand_primes):
        n += 1
      if (n > current_n):
        current_n = n
        optimal_a = a
        optimal_b = b
  return optimal_a * optimal_b

print(get_optimal_expression_ab_product()) # -59231  (But takes 9min43s)

# Correct