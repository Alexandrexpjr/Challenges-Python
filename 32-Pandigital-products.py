# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def find_sum_of_all_unusual_products():
  products = set()
  for multiplicand in range(0, 999):
    for multiplier in range(0, 9999):
      current_product = multiplicand * multiplier
      all_digits = str(multiplicand) + str(multiplier) + str(current_product)
      if (len(all_digits) == 9 and all_digits.find('0') == -1 and all(number in all_digits for number in '123456789')):
        products.add(current_product)
  return sum(products)

print(find_sum_of_all_unusual_products()) #45228

# Correct