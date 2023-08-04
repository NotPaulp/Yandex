def BFS(v,way,checked,prev,finish):
    step=0
    final_way=[]
    while step<len(way) and len(way[step])!=0:
        for vi in way[step]:


            for vi_next in v[vi]:

                if checked[vi_next]==-1:
                    way[step+1].append(vi_next)
                    prev[vi_next]=vi
                    checked[vi_next] = 1
                    if vi_next == finish:
                        current = finish
                        while current != 0:
                            final_way.append(current)
                            current = prev[current]
                        return final_way
            checked[vi]=1
        step+=1


    return final_way
V=int(input())
checked=[-1]*(V+1)
v={}
way={}
prev={}
for i in range(1,V+1):
    prev[i]=0
    v[i]=list()
    way[i-1]=list()
for i in range(V):
        row=list(map(int,input().split()))
        for j in range(len(row)):
            if row[j]==1:
                v[i+1].append(j+1)
start,finish=map(int,input().strip().split())
if start==finish:
    print(0)
else:
    way[0].append(start)
    answer=BFS(v,way,checked,prev,finish)
    print(len(answer)-1)
    if len(answer):
        print(*answer[::-1])