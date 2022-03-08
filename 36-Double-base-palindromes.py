# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(number):
  numberString = str(number)
  stringList = list(numberString)
  numberList = stringList.copy()
  stringList.reverse()
  return (stringList == numberList)

def convert_to_bin(n):
  return bin(n)[2:]

def is_double_based_palindromic_numbers(n):
  return (isPalindrome(n) and isPalindrome(convert_to_bin(n)))

def get_sum_of_double_palindromic_under_n(n):
  numbers = []
  for number in range(n):
    if is_double_based_palindromic_numbers(number):
      numbers.append(number)
  return sum(numbers)

print(get_sum_of_double_palindromic_under_n(1000000)) # 872187

# Correct