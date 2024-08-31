import heapq


def Dijkstra(start, finish, v, way):
    heap = [(0, start)]
    while heap:
        vi = heapq.heappop(heap)
        for connected_vi in v.get(vi[1], []):
            if way[vi[1]] + v[vi[1]][connected_vi] < way[connected_vi]:
                way[connected_vi] = way[vi[1]] + v[vi[1]][connected_vi]
                heapq.heappush(heap, (way[connected_vi], connected_vi))
    if way[finish] < float('inf'):
        return way[finish]
    else:
        return -1


N, K = map(int, input().split())
v = {}
way = [float('inf')] * (N + 1)
for i in range(K):
    a, b, l = map(int, input().split())
    if not (v.get(a, None)):
        v[a] = {b: l}
    else:
        v[a][b] = l
    if not (v.get(b, None)):
        v[b] = {a: l}
    else:
        v[b][a] = l
A, B = map(int, input().split())
way[A] = 0
print(Dijkstra(A, B, v, way))
