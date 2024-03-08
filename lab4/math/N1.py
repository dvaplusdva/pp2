import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degree = float(input("Input degree: "))

radian = degrees_to_radians(degree)
print(f"Output radian: {radian:.6f}")
