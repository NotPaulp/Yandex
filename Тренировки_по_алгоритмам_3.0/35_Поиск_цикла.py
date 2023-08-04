def DFS(v,checked,current,cycle,last):
    global start
    if checked[current]==0:
        checked[current] = 1
        for vi_next in v[current]:
            if checked[vi_next]!=2 and vi_next!=last:
                result=DFS(v,checked,vi_next,cycle,current)
                if result==1:
                    cycle.append(current)

                    if start==current:
                        return -1
                    else:
                        return 1
                elif result==-1:
                    return -1
    elif checked[current]==1:
        start=current
        return 1
    checked[current]=2


V=int(input())
checked=[0]*(V+1)
v={}
start=0
parents={}
for i in range(1,V+1):
    v[i]=list()
for i in range(V):
        row=list(map(int,input().split()))
        for j in range(len(row)):
            if row[j]==1:
                v[i+1].append(j+1)
final=[]
cycle=[]
for i in range(1,V+1):
    if checked[i]==0:
        DFS(v, checked, i,cycle,0)
        if len(cycle)>0:
            print('YES')
            print(len(cycle))
            print(*cycle)
            break
else:
    print('NO')