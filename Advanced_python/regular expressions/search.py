import re
words = "The ants go marching one by one"

strings = ['the', 'one']

for word in strings:
    match = re.search(word, words)
    if match:
        print('Found "{}" in "{}"'.format(word, words))
        print(words[match.start():match.end()])
    else:
        print('Did not Found {}'.format(word))
