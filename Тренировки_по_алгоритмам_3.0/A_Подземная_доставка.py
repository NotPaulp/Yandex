N=int(input())
train=[]
for i in range(N):
    request=input().split(' ')
    if request[0]=='add':
        amount=int(request[1])
        product=request[2]
        train.append([amount,product])
    elif request[0]=='delete':
        amount=int(request[1])
        for i in range(len(train)-1,-1,-1):
            if amount<train[i][0]:
                train[i][0]-=amount
                break
            else:
                amount-=train.pop()[0]
    elif request[0]=='get':
        product = request[1]
        amount=0
        for i in train:
            if i[1]==product:
                amount+=i[0]
        print(amount)

