def calculate_trapezoid_area(height, base1, base2):
    return (base1 + base2) / 2 * height

height = 5
base1 = 5
base2 = 6

area = calculate_trapezoid_area(height, base1, base2)

print(f"Expected Output: {area}")
