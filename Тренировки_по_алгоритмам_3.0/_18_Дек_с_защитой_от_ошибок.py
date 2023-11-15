def increase_back(deque,head):
    new_deque=[None]*len(deque)*2
    for i in range(len(deque)):
        new_deque[i]=deque[(i+head)%len(deque)]
    return new_deque,len(deque)
def increase_front(deque,head):
    new_deque=[None]*len(deque)*2
    head+=1
    for i in range(1,len(deque)+1):
        new_deque[i]=deque[(i-1+head)%len(deque)]
    return new_deque,len(deque)
deque=[None]*3
default_head=0
default_tail=-1
head=default_head
tail=default_tail
while True:
    command_string = input().split(' ')
    command=command_string[0]
    if command=='push_front':
        if head == 0:
            head = len(deque)-1
        else:
            head -= 1

        if tail == head and deque[tail - 1] != None:
            deque, tail = increase_front(deque, head)
            head = 0
        if tail<0:
            tail=head
        deque[head] = int(command_string[1])
        print('ok')
    elif command == 'push_back':
        if tail==len(deque)-1:
            tail=0
        else:
            tail+=1
        if tail==head and deque[tail-1]!=None:
            deque,tail=increase_back(deque,head)
            head = 0
        deque[tail]=int(command_string[1])
        print('ok')
    elif command=='pop_back':
        if deque[tail]!=None:
            print(deque[tail])
            deque[tail]=None
            if head==tail:
                head = default_head
                tail = default_tail
            else:
                if tail==0:
                    tail=len(deque)-1
                else:
                    tail-=1
        else:
            print('error')
            head = default_head
            tail = default_tail
    elif command=='pop_front':
        if deque[head]!=None:
            print(deque[head])
            deque[head]=None
            if head==tail:
                head = default_head
                tail = default_tail
            else:
                if head==len(deque)-1:
                    head=0
                else:
                    head+=1
        else:
            print('error')
            head = default_head
            tail = default_tail
    elif command=='front':
        if deque[head]!=None:
            print(deque[head])
        else:
            print('error')
    elif command=='back':
        if deque[tail]!=None:
            print(deque[tail])
        else:
            print('error')
    elif command=='size':
        print(tail-head+1+int(head>tail)*len(deque)*int(tail!=-1))
    elif command=='clear':
        for i in range(head,tail+len(deque)*int(tail<head)*int(deque[head]!=None)+1):
            deque[i%len(deque)]=None
        head=default_head
        tail=default_tail
        print('ok')
    elif command=='exit':
        print('bye')
        break
    # print(deque)
    # print(head,tail)