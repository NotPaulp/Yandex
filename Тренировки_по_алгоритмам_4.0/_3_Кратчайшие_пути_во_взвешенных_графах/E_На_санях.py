import heapq


def Dijkstra(start,  yamshik, road, time_spent):
    heap = [(0, 0, start)]
    while heap:
        currentTime, currentDistance, currentCity = heapq.heappop(heap)
        for nextCity, S in road.get(A):
            nextT, nextV = yamshik[nextCity]
            if nextT+
            heapq.heappush(heap, (arrivalTime, nextVillage))
    if time_spent[finish] < float('inf'):
        return time_spent[finish]
    else:
        return -1
    way[S] = 0
    prev = {}
    stack.append(start)
    while stack:
        vi = stack.pop()
        for connected_vi in v[vi]:
            if way[vi] + v[vi][connected_vi] < way[connected_vi]:
                way[connected_vi] = way[vi] + v[vi][connected_vi]
                prev[connected_vi] = vi
                stack.append(connected_vi)
    if way[finish] < float('inf'):
        current = finish
        path = []
        while True:
            path.append(current)
            if current == start:
                return path[::-1]
            current = prev[current]
    else:
        return [-1]


N = int(input())
yamshik = {}
time_spent = [float('inf')] * (N + 1)
for i in range(1, N + 1):
    T, V = map(int, input().split())
    yamshik[i] = (T, V)
road = {}
for j in range(1, N):
    A, B, S = map(int, input().split())
    if road.get(A,False):
        road[A].add((B, S))
    else:
        road[A] = {(B, S)}
    if road.get(B,False):
        road[B].add((A, S))
    else:
        road[B] = {(A, S)}

time_spent[i-1] = float('inf')
time_spent[i] = 0
print(Dijkstra(1, yamshik, road, time_spent))
