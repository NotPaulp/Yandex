def BFS(v,way,checked,finish):
    step=0
    while step<len(way) and len(way[step])!=0:
        for vi in way[step]:
            if vi==finish:
                return step
            for vi_next in v[vi]:
                if checked[vi_next]==-1:
                    way[step+1].append(vi_next)
            checked[vi]+=1
        step+=1


    return -1
V=int(input())
checked=[-1]*(V+1)
v={}
way={}

for i in range(1,V+1):
    v[i]=list()
    way[i-1]=list()
for i in range(V):
        row=list(map(int,input().split()))
        for j in range(len(row)):
            if row[j]==1:
                v[i+1].append(j+1)
start,finish=map(int,input().strip().split())
way[0].append(start)
print(BFS(v,way,checked,finish))