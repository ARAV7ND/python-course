import re

strings = "The ants go marching one by one"

patterns = ['The', 'ants', 'Hey']


# for word in
for pattern in patterns:
    regex = re.compile(pattern)
    if re.search(regex, strings):
        print('Found "{}" in "{}"'.format(pattern, strings))
        print(regex)
    else:
        print('Did not found "{}"'.format(pattern))
