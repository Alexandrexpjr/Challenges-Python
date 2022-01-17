# 16: 2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2 ** 1000?

very_big_number = 2 ** 1000
very_big_string = str(very_big_number) # strings are lists
sum = 0
for digit in very_big_string:
  sum += int(digit)
print(sum) # 1366

#Correct 