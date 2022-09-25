# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

def find_last_ten_digits():
  sum = 0
  for n in range(1, 1001):
    sum += n ** n
  return str(sum)[-10:]
print(find_last_ten_digits()) # 9110846700

# Correct