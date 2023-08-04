stack=[]
while True:
    command_string = input().split(' ')
    command=command_string[0]
    if command=='push':
        stack.append(int(command_string[1]))
        print('ok')
    elif command=='pop':
        if len(stack)>0:
            print(stack.pop())
        else:
            print('error')
    elif command=='back':
        if len(stack)>0:
            print(stack[len(stack)-1])
        else:
            print('error')
    elif command=='size':
        print(len(stack))
    elif command=='clear':
        stack.clear()
        print('ok')
    elif command=='exit':
        print('bye')
        break