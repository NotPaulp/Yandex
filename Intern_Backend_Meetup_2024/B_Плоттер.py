n, m = map(int, input().split())
c = int(input())
commands = input()
x, y = 0, 0
ranges = set()
for command in commands:
    if command == 'R':
        ranges.add((x, y, x + 1, y))
        x += 1
    elif command == 'L':
        ranges.add((x - 1, y, x, y))
        x -= 1
    elif command == 'U':
        ranges.add((x, y, x, y + 1))
        y += 1
    else:
        ranges.add((x, y - 1, x, y))
        y -= 1
print(len(ranges))
