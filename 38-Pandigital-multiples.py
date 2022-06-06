# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?]

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_largest_1_to_9_pandigital_number():
  largest_pandigital = 1
  for n in range(10000):
    concatenated = ''
    for integer in integers:
      concatenated += str(n * integer)

      if (len(concatenated) >= 9):
        break

    sorted = list(int(digit) for digit in concatenated)
    sorted.sort()
    if (len(concatenated) == 9 and sorted == integers):
      if (int(concatenated) > largest_pandigital):
        largest_pandigital = int(concatenated)
    
    continue
  return largest_pandigital
print(get_largest_1_to_9_pandigital_number()) # 932718654

# Correct