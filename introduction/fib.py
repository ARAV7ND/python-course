def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        a = fib(n-1)+fib(n-2)
        print('fib(',n-1,')+fib(',n-2,')=',a)
        return a
print(fib(7))