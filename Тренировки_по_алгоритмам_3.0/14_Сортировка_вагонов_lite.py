def check(train):
    buffer = []
    next_carriage = 1

    for carriage in train:
        while buffer and buffer[-1] == next_carriage:
            buffer.pop()
            next_carriage += 1

        if carriage == next_carriage:
            next_carriage += 1
        else:
            buffer.append(carriage)

    while buffer and buffer[-1] == next_carriage:
        buffer.pop()
        next_carriage += 1

    return next_carriage == len(train) + 1
n = int(input())
train = list(map(int, input().split()))
result = check(train)
if result:
    print("YES")
else:
    print("NO")