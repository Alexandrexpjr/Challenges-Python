# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def sortDigits(n):
  digitList = list(str(n))
  digitList.sort()
  return int(''.join(digitList))

def isPermutedMultiple(n):
  return sortDigits(n) == sortDigits(2*n) == sortDigits(3*n) == sortDigits(4*n) == sortDigits(5*n) == sortDigits(6*n)

def getPermutedMultiple():
  answer = 0
  count = 1
  while (answer == 0):
    if isPermutedMultiple(count):
      answer = count
    count += 1
  return answer

print(getPermutedMultiple()) # 142857

# Correct