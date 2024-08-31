from collections import deque
def BFS(V, deletes):
    repositories = deque([0])
    while repositories:
        repository = repositories.popleft()
        for child_repository in V[repository]:
                deletes[child_repository]=deletes[repository]+1
                repositories.append(child_repository)
N=int(input())
V={}
deletes=[0]*(N+1)
parents={}
for i in range(0,N+1):
    V[i]=list()
for i in range(1,N+1):
    R=int(input())
    V[R].append(i)
BFS(V,deletes)
print(deletes.index(max(deletes)))
