import sys
def DFS(v,checked,current,parents,final):
    checked[current]=1
    for vi in v[current]:
        if checked[vi]==0:
            if DFS(v,checked,vi,parents,final)==-1:
                return -1
        elif checked[vi]==1:
            return -1
        parents[vi]-=1
    checked[current]=2
    final.append(current)
sys.setrecursionlimit(200000)
V,E=map(int,input().split(' '))
checked=[0]*(V+1)
v={}
parents={}
for i in range(1,V+1):
    v[i]=list()
    parents[i]=0
for i in range(E):
    f,s=map(int,input().split())
    v[f].append(s)
    parents[s]+=1
final=[]
for i in range(1,V+1):
    if parents[i]==0 and checked[i]==0:
        if DFS(v, checked, i,parents, final)==-1:
            break
if len(final)==V:
    print(*final[::-1])
else:
    print(-1)