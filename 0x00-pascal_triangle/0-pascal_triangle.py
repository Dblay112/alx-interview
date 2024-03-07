#!/usr/bin/python3
def pascal_triangle(n):
if n <= 0:
    return []

  triangle = [[1] for _ in range(n)]  # Initialize triangle with 1s in each row

  for i in range(2, n):
    # Iterate through rows starting from the second row (i=2)
    for j in range(1, i):
      # Fill inner elements by adding elements above
      triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

    # Add 1 at the end of each row
    triangle[i].append(1)

  return triangle
