# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# i'll check all numbers below 360000, which have 6 digits, because 9 ** 5 = 59.049 ( ~60k), and 6*60 = 360.000 (6 digits).
# If i try 7 digits, 60 * 7 = 420k, which also have 6 digits.

def check_sum_of_five_power_digits(n):
  digits = list(str(n))
  sum = 0
  for index, digit in enumerate(digits):
    digits[index] = int(digit) ** 5
    sum += digits[index]
  return (n == sum)

def find_numbers_written_as_fifth_power_sum():
  max_number = 360000
  first_number = 2
  numbers = []
  sum = 0
  for number in range(first_number, max_number):
    if(check_sum_of_five_power_digits(number)):
      numbers.append(number)
      sum += number
  return sum

print(find_numbers_written_as_fifth_power_sum()) # 443839 (1s)

# Correct