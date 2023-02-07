from collections import deque
import string

d = deque(string.ascii_lowercase)

for letter in d:
    # d.append(letter)
    print(letter)

print(d)
d.append('xyz')
print(d)
