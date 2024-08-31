import heapq


def Dijkstra(start, finish, v, time_spent):
    heap = [(0, start)]
    while heap:
        currentTime, currentVillage = heapq.heappop(heap)
        for nextVillage, departureTime, arrivalTime in v.get(currentVillage, {(None, -1, -1)}):
            if departureTime >= currentTime and arrivalTime < time_spent[nextVillage]:
                time_spent[nextVillage] = arrivalTime
                heapq.heappush(heap, (arrivalTime, nextVillage))
    if time_spent[finish] < float('inf'):
        return time_spent[finish]
    else:
        return -1


N = int(input())
village_d, village_v = map(int, input().split())
R = int(input())
v = {}
time_spent = [float('inf')] * (N + 1)
for i in range(R):
    A, t1, B, t2 = map(int, input().split())
    if not (v.get(A, None)):
        v[A] = {(B, t1, t2)}
    else:
        v[A].add((B, t1, t2))
time_spent[village_d] = 0
print(Dijkstra(village_d, village_v, v, time_spent))
