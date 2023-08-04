def BFS(v,way,start):
    step=0
    while step<len(way) and len(way[step])!=0:
        for vi in way[step]:
            if vi<V*V:
                return step
            if vi>=V*V:
                vi_next=vi-V*V
                if v[vi_next] =='.':
                    way[step+1].append(vi_next)
                    v[vi_next]="#"
            if vi<(V-1)*V*V:
                vi_next=vi+V*V
                if v[vi_next] =='.':
                    way[step+1].append(vi_next)
                    v[vi_next]="#"
            if vi%(V*V)>=V:
                vi_next=vi-V
                if v[vi_next] =='.':
                    way[step+1].append(vi_next)
                    v[vi_next]="#"
            if vi % (V * V) < V*(V-1):
                vi_next = vi + V
                if v[vi_next]  == '.':
                    way[step + 1].append(vi_next)
                    v[vi_next] = "#"
            if vi % (V) > 0:
                vi_next = vi - 1
                if v[vi_next]  == '.':
                    way[step + 1].append(vi_next)
                    v[vi_next] = "#"
            if vi % (V) < V-1:
                vi_next = vi + 1
                if v[vi_next] == '.':
                    way[step + 1].append(vi_next)
                    v[vi_next] = "#"
        step+=1


    return -1
V=int(input())
input()

v={}
way={}

for i in range(V**3):

    way[i]=list()
for z in range(V):
    for y in range(V):
        cave=input()
        for x in range(V):
            if cave[x]=='S':
                start=z*V*V+y*V+x
            v[z*V*V+y*V+x]=cave[x]
    if z<V-1:input()
way[0].append(start)
print(BFS(v,way,start))