def DFS(v,checked,current):
    global components
    checked[current]=True
    for vi in v[current]:
        if checked[vi]==False:
            components.append(vi)
            DFS(v,checked,vi)
V,E=map(int,input().split(' '))
checked=[False]*(V+1)
v={}
components=[1]
for i in range(1,V+1):
    v[i]=list()
for i in range(E):
    f,s=map(int,input().split())
    v[f].append(s)
    v[s].append(f)
DFS(v,checked,1)
print(len(components))
print(*sorted(components))
