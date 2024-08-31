
n, m = map(int, input().split())
events = []

for _ in range(n):
    a, b = map(int,input().split())
    events.append([a, -1, None])
    events.append([b, 1, None])
points = list(map(int, input().split()))

for i in range(len(points)):
    events.append([points[i], 0, i])

events.sort()

answer = [0] * m
currentRanges = 0

for point, type, i in events:
    if type == -1:
        currentRanges += 1
    elif type == 1:
        currentRanges -= 1
    else:
        answer[i] = currentRanges
print(*answer)
