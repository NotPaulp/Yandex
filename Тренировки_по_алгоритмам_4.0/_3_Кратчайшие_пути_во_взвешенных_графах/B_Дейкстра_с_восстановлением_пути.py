import collections


def Dijkstra(start,finish,v,way):
    stack=collections.deque()
    way[S]=0
    prev={}
    stack.append(start)
    while stack:
        vi=stack.pop()
        for connected_vi in v[vi]:
            if way[vi]+v[vi][connected_vi]<way[connected_vi]:
                way[connected_vi]=way[vi]+v[vi][connected_vi]
                prev[connected_vi]=vi
                stack.append(connected_vi)
    if way[finish]<float('inf'):
        current=finish
        path=[]
        while True:
            path.append(current)
            if current==start:
                return path[::-1]
            current=prev[current]
    else:
        return [-1]
N,S,F=map(int,input().split())
v={}
for i in range(1,N+1):
    edges=list(map(int,input().split()))
    v[i]={}
    for n in range(len(edges)):
        if edges[n]>0:
            v[i][n+1]=edges[n]
way=[float('inf')]*(N+1)
print(*Dijkstra(S,F,v,way))
