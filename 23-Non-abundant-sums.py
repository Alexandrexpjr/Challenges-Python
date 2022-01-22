# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def get_divisors(n):
  divisors = []
  for number in range(1, n):
    if (n % number == 0):
      divisors.append(number)
  return divisors

def sum_of_numbers(numbers_list):
  sum = 0
  for number in numbers_list:
    sum += number
  return sum

def is_abundant(n):
  return (n < sum_of_numbers(get_divisors(n)))

print(is_abundant(12))

def get_abundant_numbers_under_n(n):
  abundants = []
  for number in range(1, n + 1):
    if (is_abundant(number)): abundants.append(number)
  return abundants

def get_all_possible_abundant_sums_under_n(n):
  abundants = get_abundant_numbers_under_n(n)
  possible_sums = []
  for abundant in abundants:
    for ab in abundants:
      possible_sums.append(abundant + ab)
  return possible_sums


def get_numbers_out_of_list(number_list, max):
  numbers_out = []
  for number in range(1, max + 1):
    if (number_list.count(number) == 0): numbers_out.append(number)
  return numbers_out

def sum_of_list_numbers(number_list):
  sum = 0
  for number in number_list:
    sum += number
  return sum

def non_abundant_sums(max_number):
  possible_sums = get_all_possible_abundant_sums_under_n(max_number)
  numbers_out = get_numbers_out_of_list(possible_sums, max_number)
  return sum_of_list_numbers(numbers_out)

print(non_abundant_sums(28123))
