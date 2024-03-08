import math

def regular_polygon_area(n_sides, side_length):
    area = (n_sides * (side_length ** 2)) / (4 * math.tan(math.pi / n_sides))
    return area

n_sides = 4
side_length = 25

area = regular_polygon_area(n_sides, side_length)
print(f"The area of the polygon is: {area}")
