# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

def is_right_angled_triangle(a, b, c):
  hypotenuse = max(a,b,c)
  legs = [a, b, c]
  legs.remove(hypotenuse)
  return hypotenuse ** 2 == sum(list(leg ** 2 for leg in legs))

def get_right_angled_triangles_by_perimeter_p(p):
  triangles = set()
  for a in range(1, int(p/2)):
    for b in range(1, int(p/2)):
      c = p - (a + b)
      if (is_right_angled_triangle(a, b, c)):
        triangle = [a, b, c]
        triangle.sort()
        triangles.add(tuple(triangle))
  return triangles

def maximize_perimeters_where_p_below_n(n):
  maximized = 0
  solutions = 0
  for perimeter in range(6, n):
    triangles = get_right_angled_triangles_by_perimeter_p(perimeter)
    if (len(triangles) > solutions):
      solutions = len(triangles)
      maximized = perimeter
  return maximized

print(maximize_perimeters_where_p_below_n(1000)) # 840

# Correct