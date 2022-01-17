# 15: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

# To solve, i had a look at https://mathigon.org/task/paths-on-a-grid to understand the logic
# In practice I need to calculate the combination of the number of steps taking the paths, C(40, 20)
# C(n, m) = (n!) / m!(n - m)! => https://en.wikipedia.org/wiki/Combination

def factorial(n):
  factorial = n
  for number in range(1, n):
    factorial *= number
  return factorial

def combination(n, m):
  return factorial(n) / (factorial(m) * factorial(n - m))

print(combination(40, 20)) # 137846528820

# Correct

    