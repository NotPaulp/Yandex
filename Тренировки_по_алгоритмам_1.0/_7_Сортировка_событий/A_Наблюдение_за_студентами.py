def binary_search(supervised, newEvent):
    point, type = newEvent
    L = 0
    R = len(supervised) - 1
    while L <= R:
        C = (L + R) // 2
        pointAtCenter = supervised[C][0]
        typeAtCenter = supervised[C][1]
        if point > pointAtCenter:
            L = C + 1
        elif point < pointAtCenter:
            R = C - 1
        else:
            if typeAtCenter > type:
                return C
            else:
                return C + 1
    return L


N, M = map(int, input().split())
supervised = []
for _ in range(M):
    b, e = map(int, input().split())
    newStart = (b, 1)
    newStop = (e, 2)
    insertIndex = binary_search(supervised, newStart)
    supervised.insert(insertIndex, newStart)
    insertIndex = binary_search(supervised, newStop)
    supervised.insert(insertIndex, newStop)
supervised.append((N, 1))
currentlyLooking = 0
lastStopPoint = -1
unsupervisedCount = 0
for event in supervised:
    point, type = event
    if currentlyLooking < 1:
        unsupervisedCount += point - lastStopPoint - 1
    if type == 1:
        currentlyLooking += 1
    else:
        currentlyLooking -= 1
        lastStopPoint = point
print(unsupervisedCount)
