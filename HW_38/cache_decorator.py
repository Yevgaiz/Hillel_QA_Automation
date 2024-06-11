import functools
import math


def result_cache_decorator(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print(f"From cache: args={args}, kwargs={kwargs}")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"Calculate and save: args={args}, kwargs={kwargs}")
        return result

    return wrapper


@result_cache_decorator
def custom_sqrt(x):
    return math.sqrt(x)


@result_cache_decorator
def custom_add(a, b, c):
    return a, b, c


print(custom_sqrt(4))
print(custom_sqrt(4))
print(custom_sqrt(x=4))
print(custom_sqrt(x=4))

print(custom_add(a=4, b=2, c=3))
print(custom_add(c=3, b=2, a=4))
