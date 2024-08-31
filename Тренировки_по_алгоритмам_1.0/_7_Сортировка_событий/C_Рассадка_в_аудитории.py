from collections import deque

N, D = map(int, input().split())
Xs = list(map(int, input().split()))
events = []
for i in range(len(Xs)):
    events.append([Xs[i], -1, i])
    events.append([Xs[i] + D, 1, None])
events.sort()
currentIntersections = 0
answer = [0] * N
var = 0
availableVars = deque([1])
usedVars = deque()
maxVar = 0
for X, type, i in events:
    if type == -1:
        currentIntersections += 1
        if len(availableVars) == 0:
            availableVars.append(len(usedVars) + 1)
        usedVars.append(availableVars.popleft())
        answer[i] = usedVars[-1]
        maxVar = max(currentIntersections, maxVar)
    elif type == 1:
        availableVars.append(usedVars.popleft())
        currentIntersections -= 1
print(maxVar)
print(*answer)
