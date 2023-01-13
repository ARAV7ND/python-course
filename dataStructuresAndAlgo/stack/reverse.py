from stack import Stack

def reverse(string):
    rev_string=''
    stack = Stack()
    for i in string:
        stack.push(i)
    while(not stack.is_empty()):
        rev_string+=stack.pop()
    return rev_string

print("reverse of vamshi",reverse('vamshi'))
