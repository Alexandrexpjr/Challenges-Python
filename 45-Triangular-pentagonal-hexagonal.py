# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

def get_n_pentagonals(min_size, max_size):
  n = min_size
  pentagonals = []
  while(len(pentagonals) < max_size):
    Pn = n*(3*n - 1) / 2
    pentagonals.append(Pn)
    n += 1
  return pentagonals

def get_n_triangle(min_size, max_size):
  n = min_size
  triangles = []
  while(len(triangles) < max_size):
    Tn = n*(n + 1) / 2
    triangles.append(Tn)
    n += 1
  return triangles

def get_n_hexagonals(min_size, max_size):
  n = min_size
  hexagonals = []
  while(len(hexagonals) < max_size):
    Hn = n*(2*n - 1)
    hexagonals.append(Hn)
    n += 1
  return hexagonals

def get_answer(min_size, max_size):
  triangles = get_n_triangle(min_size, max_size)
  pentagonals = get_n_pentagonals(min_size, max_size)
  hexagonals = get_n_hexagonals(min_size, max_size)

  for hexagonal in hexagonals:
    if(hexagonal in triangles and hexagonal in pentagonals):
      return hexagonal
    if(hexagonal > triangles[-1]): return None

print(get_answer(286, 60000)) # 1533776805

# Correct