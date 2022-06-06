# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

def get_all_seven_digits_pandigital():
  pandigital = []
  digits = ['1', '2', '3', '4', '5', '6', '7'] #every pandigital with 8 and 9 digits are multiple of 3 (1+2+...8 = 36 and 1+2+...9 = 45)
  for number in range(1234567, 7654322):
    sorted = list(str(number))
    sorted.sort()
    if (sorted == digits):
      pandigital.append(number)
  return pandigital

def get_largest_pandigital_prime():
  pandigital = get_all_seven_digits_pandigital()
  biggest = 0
  for pand in pandigital[::-1]:
    for number in range(2, pand):
      if (pand % number == 0):
        break
      if (number == (pand - 1)):
        biggest = pand
    if (biggest != 0): break
  return biggest

print(get_largest_pandigital_prime()) # 7652413

# Correct