# Memoized Fibonacci
# Speed up with cache
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
