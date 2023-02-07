from functools import partial


def add(a, b):
    return a+b


add_one = partial(add, 1)
print(add_one(5))

add_two = partial(add, a=2)
print(add_two(b=5))
