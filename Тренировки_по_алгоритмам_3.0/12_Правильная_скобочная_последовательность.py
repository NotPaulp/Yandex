stack=[]
s=input()
for i in s:
    if i==']':
        if len(stack)>0:
            if stack[-1]=='[':
                stack.pop()
            else:
                print('no')
                break
        else:
            print('no')
            break
    elif i==')':
        if len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        else:
            print('no')
            break
    elif i=='}':
        if len(stack) > 0:
            if stack[-1] == '{':
                stack.pop()
            else:
                print('no')
                break
        else:
            print('no')
            break
    else:
        stack.append(i)

else:
    if len(stack)>0:
        print('no')
    else:
        print('yes')

