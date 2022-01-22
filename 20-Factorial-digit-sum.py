# 20 Factorial digit sum

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def get_factorial(n):
  factorial = 1
  for number in range(n, 0, -1):
    factorial *= number
  return factorial

def digits_sum(n):
  sum = 0
  number_to_string_list = list(str(n))
  for number in number_to_string_list:
    sum += int(number)
  return sum

print(digits_sum(get_factorial(100))) # 648

# Correct
