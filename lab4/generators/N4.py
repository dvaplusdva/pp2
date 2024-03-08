def squares(a, b):
    for number in range(a, b + 1):
        yield number ** 2

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

for square in squares(a, b):
    print(square)
