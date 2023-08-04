N, M, K = map(int, input().split())
prefm = []

for i in range(N):
    row = list(map(int, input().split()))
    prefm.append(row)

    for j in range(M):
        if i > 0 and j > 0:
            prefm[i][j] += prefm[i - 1][j] + prefm[i][j - 1] - prefm[i - 1][j - 1]
        elif i > 0:
            prefm[i][j] += prefm[i - 1][j]
        elif j > 0:
            prefm[i][j] += prefm[i][j - 1]

result = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    if x1 > 0 and y1 > 0:
        res = (
            prefm[x2][y2]
            - prefm[x1 - 1][y2]
            - prefm[x2][y1 - 1]
            + prefm[x1 - 1][y1 - 1]
        )
    elif x1 > 0:
        res = prefm[x2][y2] - prefm[x1 - 1][y2]
    elif y1 > 0:
        res = prefm[x2][y2] - prefm[x2][y1 - 1]
    else:
        res = prefm[x2][y2]

    result.append(res)

for res in result:
    print(res)