def fib(n):
    a, b = 1, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib(10))

e = input()
print(e, "=", eval(e))
