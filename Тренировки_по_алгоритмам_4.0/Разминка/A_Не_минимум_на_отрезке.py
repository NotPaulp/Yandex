N, M = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(M):
    L, R = map(int, input().split())
    amax = max(a[L:(R + 1)])
    amin = min(a[L:(R + 1)])
    if amax != amin:
        print(amax)
    else:
        print("NOT FOUND")
