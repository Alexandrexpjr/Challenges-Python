# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#                              21 22 23 24 25
#                              20  7  8  9 10
#                              19  6  1  2 11
#                              18  5  4  3 12
#                              17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def diagonal_sum_of_n_spiral(n):
  first_number = 3
  sum = 1
  spiral = 1
  current_increment = 2
  while(spiral < (n + 1) / 2):
    last_number = first_number + (3 * current_increment)
    for number in range(first_number, last_number + 1, current_increment):
      sum += number
      if number == last_number:
        current_increment += 2
        first_number = last_number + current_increment
        spiral += 1
        break
  return sum

print(diagonal_sum_of_n_spiral(1001)) # 669171001 (0s)

#Correct