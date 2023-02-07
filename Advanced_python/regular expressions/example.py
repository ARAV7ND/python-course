import re

text = 'abcdefgh'

parser = re.search('a[b-f]*f', text)
print(parser)
print(parser.group())
