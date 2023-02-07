from functools import lru_cache

# withour chache


def fib(n):
    if n < 2:
        return n
    print(f"calculating for {n}")
    return fib(n-1) + fib(n-2)


# print(fib(10))

@lru_cache(maxsize=5)
def fib_cache(n):
    if n < 2:
        return n
    print(f"calculating for {n}")
    return fib_cache(n-1) + fib_cache(n-2)


print(fib_cache(10))
print(fib_cache.cache_info())
