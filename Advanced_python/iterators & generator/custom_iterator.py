class MyIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        letter = self.data[self.position]
        self.position += 1
        return letter


arr = [1, 2, 3, 4]
iter_obj = MyIterator(arr)
my_iter = iter_obj.__iter__()
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
# print(my_iter.__next__())
