def my_generator():
    yield "one"
    yield "two"
    yield "three"


my_gen = my_generator()
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
for item in my_gen:
    print(item)
print(my_gen)
print(next(my_gen))
