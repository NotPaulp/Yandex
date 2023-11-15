from math import *
def BFS(v,way,checked,lines):
    step=0
    final=-1
    while way[step]:
        for vi in way[step]:
            if B in lines[vi]:
                if final!=-1:
                    if final>step:
                        final=step
                else:
                    final=step
            for vi_next in v[vi]:
                if checked[vi_next]==-1:
                    way[step+1].append(vi_next)
                    checked[vi_next] = 1
        step+=1
    return final
N=int(input())
M=int(input())
lines=[]
v={}
way={}
checked=[-1]*M
for i in range(M):
    v[i]=list()
    way[i]=list()
way[M]=None
for i in range(M):
    line=(input().strip().split(' '))[1:]
    lines.append(set(map(int,line)))
    for j in range(i):
        if not(lines[i].isdisjoint(lines[j])):
            v[i].append(j)
            v[j].append(i)
A,B=map(int,input().strip().split(' '))
for i in range(M):
    if A in lines[i]:
        way[0].append(i)
        checked[i]=1
print(BFS(v,way,checked,lines))



