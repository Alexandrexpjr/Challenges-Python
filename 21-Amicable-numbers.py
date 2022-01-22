# 21: Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

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

def is_amicable(n):
  n_divisors = get_divisors(n)
  n_divisors_sum = sum_of_numbers(n_divisors)
  d = n_divisors_sum
  d_divisors = get_divisors(d)
  d_divisors_sum = sum_of_numbers(d_divisors)

  if (n == d_divisors_sum) and not (n == n_divisors_sum) :
    return True
  return False

is_amicable(496)

def get_sum_of_amicables_under_n(n):
  sum = 0
  for number in range(1, n + 1):
    if is_amicable(number):
      sum += number
  return sum

get_sum_of_amicables_under_n(10000)