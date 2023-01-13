from stack import Stack
def is_balanced(string):
    stack = Stack()
    print('str',string)
    for i in string:
        if(i == '[' or i=='{' or i=='('):
            stack.push(i)
        else:
            pop = stack.pop()
            if(i == ']' and not (pop == '[')):
                return False
            if(i == '}' and not (pop == '{')):
                return False
            if(i == ')' and not (pop == '(')):
                return False
    return stack.is_empty()

print(is_balanced("[[[{}}{}]]"))

            