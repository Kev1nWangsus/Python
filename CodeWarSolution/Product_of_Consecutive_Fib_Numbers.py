# Product of Consecutive Fibonacci Numbers

# Using Memoized Fibs
cache = {}    
def fibonacci(n):
    if n not in cache.keys():
        cache[n] = _fibonacci(n)
    return cache[n]

def _fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
def productFib(prod):
    n = 0
    while fibonacci(n) * fibonacci(n+1) < prod:
        n += 1
    return [fibonacci(n), fibonacci(n+1), fibonacci(n)*fibonacci(n+1) == prod]
    
# Raw solution
def productFib(prod):
    a = 0
    b = 1
    while a * b < prod:
        a, b = b, a+b
    return [a, b, a * b == prod]
    
