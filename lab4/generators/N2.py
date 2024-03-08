def even_numbers_generator(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i

N = int(input())

x = ', '.join(str(i) for i in even_numbers_generator(N))

print(x)
