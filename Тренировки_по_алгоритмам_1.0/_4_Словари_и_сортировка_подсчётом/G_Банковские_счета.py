import sys
clients={}
text=sys.stdin.read()
text=text.strip().split('\n')
try:
    for recording in text:
        recording=recording.split()
        operation=recording[0]
        if operation=='DEPOSIT':
            client=recording[1]
            summ=int(recording[2])
            clients[client]=clients.get(client,0)+summ
        elif operation=='WITHDRAW':
            client = recording[1]
            summ = int(recording[2])
            clients[client] = clients.get(client, 0) - summ
        elif operation=='BALANCE':
            client = recording[1]
            print(clients.get(client,'ERROR'))
        elif operation=='TRANSFER':
            client1=recording[1]
            client2=recording[2]
            summ=int(recording[3])
            clients[client1] = clients.get(client1, 0) - summ
            clients[client2] = clients.get(client2, 0) + summ
        elif operation=='INCOME':
            percent=int(recording[1])
            for client in clients:
                if clients[client]>0:
                    clients[client]=int(clients[client]*(1+(percent/100)))
except IndexError:
    pass