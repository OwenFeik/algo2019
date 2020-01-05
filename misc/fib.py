def fib(n):
    if n in [1,2]:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(10000))