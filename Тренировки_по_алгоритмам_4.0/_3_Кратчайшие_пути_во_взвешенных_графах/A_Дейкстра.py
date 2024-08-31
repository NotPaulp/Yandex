import collections


def Dijkstra(start, finish, v, way):
    stack = collections.deque()
    way[S] = 0
    stack.append(start)
    while stack:
        vi = stack.pop()
        for connected_vi in v[vi]:
            if way[vi] + v[vi][connected_vi] < way[connected_vi]:
                way[connected_vi] = way[vi] + v[vi][connected_vi]
                stack.append(connected_vi)
    return way[finish]


N, S, F = map(int, input().split())
v = {}
for i in range(1, N + 1):
    edges = list(map(int, input().split()))
    v[i] = {}
    for n in range(len(edges)):
        if edges[n] > 0:
            v[i][n + 1] = edges[n]
way = [float('inf')] * (N + 1)
shortest_path = Dijkstra(S, F, v, way)
if shortest_path < float('inf'):
    print(shortest_path)
else:
    print(-1)
