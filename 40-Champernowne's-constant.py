# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def create_irrational_decimal_fraction_with_n_digits(n):
  decimal = str()
  curr = 0
  while (len(decimal) <= 10 ** n):
    decimal += str(curr)
    curr += 1
  return decimal

def d(n):
  very_big_decimal = create_irrational_decimal_fraction_with_n_digits(6)
  return very_big_decimal[n]

def get_value_of_expression():
  return int(d(1)) * int(d(10)) * int(d(100)) * int(d(1000)) * int(d(10000)) * int(d(100000)) * int(d(1000000))

print(get_value_of_expression()) # 210

# Correct