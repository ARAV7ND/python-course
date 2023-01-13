from stack import Stack

number = 5
stack = Stack()
while(number>0):
    stack.push(number%2)
    number//=2
print("result of 10000:",end='')
while(not stack.is_empty()):
    print(stack.pop(),sep='',end='')
print()