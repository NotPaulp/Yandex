N = int(input())
events = []
for i in range(N):
    openHours, openMinutes, closingHours, closingMinutes = map(int,input().split())
    openTime = 60 * openHours + openMinutes
    closingTime = 60 * closingHours + closingMinutes
    events.append([openTime, 1, i])
    events.append([closingTime, -1, i])
events.sort()
allOpenedPeriod = 0
currentlyOpen = set()
for time, type, i in events:
    if type == 1:
        currentlyOpen.add(i)
        lastOpen = time - 24 * 60
    else:
        currentlyOpen.discard(i)
for time, type, i in events:
    if type == 1:
        currentlyOpen.add(i)
        lastOpen = time
    else:
        if len(currentlyOpen) == N:

            allOpenedPeriod += time - lastOpen
        currentlyOpen.discard(i)
print(allOpenedPeriod)
