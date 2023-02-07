from collections import Counter

# print(Counter("linustorvalds"))

counter = Counter("stevejobs")

# print(counter['s'])
print(counter.elements())


# most common
print(counter.most_common(2))

# subtract
counter_one = Counter({1: 2, 2: 3, 3: 4})
print(counter_one)
counter_two = Counter({3: 2, 2: 1, 1: 0})
counter_one.subtract(counter_two)
print(counter_one)
