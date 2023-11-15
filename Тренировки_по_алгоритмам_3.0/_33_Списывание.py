def DFS(v,current,color,colors):
    colors[current]=color
    for vi in v[current]:
        if colors[vi]==0:
            if DFS(v,vi,3-color,colors)=='NO':
                return 'NO'
        elif colors[vi]==color:
            return 'NO'

V,E=map(int,input().split(' '))
colors=[0]*(V+1)
v={}
for i in range(1,V+1):
    v[i]=list()
for i in range(E):
    f,s=map(int,input().split())
    v[f].append(s)
    v[s].append(f)
result='YES'
for i in range(1,V+1):
    if colors[i]==0:
        if DFS(v,i,1,colors)=='NO':
            result='NO'
            break
print(result)