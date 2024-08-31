import math

events = input()
mostPositive = min(events)
mostNegative = max(events)
mostPositiveIndex = len(events)
mostNegativeIndex = len(events)
minLength = float('inf')
clip = (0, len(events) - 1)
for i, event in enumerate(events):
    if event == mostPositive:
        mostPositiveIndex = i
        if math.fabs(mostPositiveIndex - mostNegativeIndex) < minLength:
            minLength = math.fabs(mostPositiveIndex - mostNegativeIndex)
            clip = (min(mostPositiveIndex, mostNegativeIndex), max(mostPositiveIndex, mostNegativeIndex))
    elif event == mostNegative:
        mostNegativeIndex = i
        if math.fabs(mostPositiveIndex - mostNegativeIndex) < minLength:
            minLength = math.fabs(mostPositiveIndex - mostNegativeIndex)
            clip = (min(mostPositiveIndex, mostNegativeIndex), max(mostPositiveIndex, mostNegativeIndex))
print(events[clip[0]:clip[1]+1])