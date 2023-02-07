from functools import reduce

arr = [1, 2, 4, 5, 3]

print(reduce(lambda x, y: x+y, arr))
print(reduce(lambda x, y: x+y, arr, 10))
