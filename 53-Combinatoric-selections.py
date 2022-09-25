# Combinatoric selections
# https://projecteuler.net/problem=53

def factorial(n):
  f = 1
  for n in range(1, n + 1):
    f *= n
  return f
  

def getCombinations(n, r):
  return factorial(n) / (factorial(r) * factorial(n - r))

def getCombinationsOverM(M):
  comb = 0
  for n in range(1, 101):
    for r in range(n):
      if (getCombinations(n, r) > M):
        comb += 1
  return comb

print(getCombinationsOverM(1000000)) # 4075

#Correct