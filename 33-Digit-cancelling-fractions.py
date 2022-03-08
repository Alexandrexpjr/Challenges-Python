# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def is_curious(numerator, denominator):
  if (numerator == denominator or (numerator % 10 == 0 and denominator % 10 == 0)):
    return False
  numerator_digits = list(str(numerator))
  denominator_digits = list(str(denominator))

  for number in numerator_digits:
    if number in denominator_digits:
      if (number == 0):
        return False
      if(len(numerator_digits) == 1 or len(denominator_digits) == 1):
        break
      numerator_digits.remove(number)
      denominator_digits.remove(number)
  new_numerator = int(''.join(numerator_digits))
  new_denominator = int(''.join(denominator_digits))
  if (new_denominator == 0 or new_numerator == numerator): return False
  return (numerator / denominator == new_numerator / new_denominator )

is_curious(12, 21)

def get_all_curious():
  curious = []
  denominators = []
  numerators = []
  for numerator in range(10, 100):
    for denominator in range(10, 100):
      if (numerator >= denominator):
        continue
      if(is_curious(numerator, denominator)):
        denominators.append(denominator)
        numerators.append(numerator)
        curious.append(str(numerator) + '/' + str(denominator))

  return {
       "curious": curious,
       "numerators": numerators,
       "denominators": denominators,
      }

print(get_all_curious())

def get_product_of_curious():
  curious_denominators = get_all_curious()['denominators']
  curious_numerators = get_all_curious()['numerators']
  denominator = 1
  numerator = 1
  for d in curious_denominators:
    denominator *= d

  for n in curious_numerators:
    numerator *= n

  div = 2
  while(div < denominator):
    if(denominator % div == 0 and numerator % div == 0):
      denominator /= div
      numerator /= div
      continue
    div += 1
  return denominator

print(get_product_of_curious()) # 100.0

# Correct