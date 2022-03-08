# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(n):
  f = 1
  for n in range(1, n + 1):
    f *= n
  return f

def sum_of_digits_factorial(n):
  digits = list(str(n))
  sum = 0
  for digit in digits:
    sum += factorial(int(digit))
  return sum

print(factorial(3))

def is_factorial_curious(n):
  return (n == sum_of_digits_factorial(n))

def get_all_factorial_curious_sum():
  sum = 0
  for n in range(3, 1000000): # 5 digits => 40730  6 digits => 40730
    if(is_factorial_curious(n)): sum += n
  return sum

print(get_all_factorial_curious_sum()) # 40730

# Correct