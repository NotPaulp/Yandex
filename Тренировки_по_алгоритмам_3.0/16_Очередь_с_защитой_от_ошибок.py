def increase(queue,head):
    N=len(queue)
    new_queue=[None]*N*2
    for i in range(N):
        new_queue[i]=queue[(i+head)%len(queue)]
    return new_queue,N
queue=[None]*100
head=0
tail=-1
while True:
    command_string = input().split(' ')
    command=command_string[0]
    if command=='push':
        if tail==len(queue)-1:
            tail=0
        else:
            tail+=1
        if tail==head and queue[tail-1]!=None:
            queue,tail=increase(queue,head)
            head = 0
        queue[tail]=int(command_string[1])
        print('ok')
    elif command=='pop':
        if queue[head]!=None:
            print(queue[head])
            queue[head]=None
            if head ==tail:
                head=0
                tail=-1
            else:
                if head==len(queue)-1:
                    head=0
                else:
                    head+=1
        else:
            print('error')
            head=0
            tail=-1
    elif command=='front':
        if queue[tail]!=None:
            print(queue[head])
        else:
            print('error')
    elif command=='size':
        print(tail-head+1+int(head>tail)*len(queue)*int(queue[head]!=None))
    elif command=='clear':
        for i in range(head,tail+len(queue)*int(tail<head)*int(queue[head]!=None)+1):
            queue[i%len(queue)]=None
        head=0
        tail=-1
        print('ok')
    elif command=='exit':
        print('bye')
        break