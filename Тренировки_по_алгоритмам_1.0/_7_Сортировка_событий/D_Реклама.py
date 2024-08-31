N = int(input())
events = []
for _ in range(N):
    enterTime, exitTime = map(int, input().split())
    if exitTime - enterTime >= 5:
        events.append([enterTime, -1])
        events.append([exitTime, 1])


