numbers = range(100)
prime_numbers = filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers)
print(list(prime_numbers))
