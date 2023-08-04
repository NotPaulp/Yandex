stack=[]
expression=input().split(' ')
for i in expression:
    if i.isdigit():
        stack.append(int(i))
    else:
        b=stack.pop()
        a=stack.pop()
        if i=='+':
            stack.append(a+b)
        elif i=='-':
            stack.append(a - b)
        elif i=='*':
            stack.append(a * b)
print(stack.pop())
