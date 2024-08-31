n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if a % 2 == b % 2 and b % 2 == c % 2:
        print('No')
    else:
        print('Yes')
