ex1
def squares_generator(N):
    for i in range(1, N + 1):
        yield i ** 2


N = 5
squares = squares_generator(N)
for square in squares:
    print(square)
ex2
def even(num):
    for i in range(num+1):
        if i%2 == 0:
            yield i

a = int(input())
print(*even(a))
ex3
def div(num):
    for i in range(num+1):
        if i%3 == 0 and i%4 == 0:
            yield i

a = int(input())
print(*div(a))
ex4
def square(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())
print(*square(a, b))
ex5
def down(a):
    while a>=0:
        yield a
        a -= 1
        

a = int(input())
print(*down(a))
