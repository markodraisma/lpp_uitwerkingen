def fibo(max):
    a, b = 0, 1
    while a<=max:
        yield a
        a, b = b, a+b

for val in fibo(250):
    print(val)

