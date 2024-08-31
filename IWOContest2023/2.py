n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
dp=[[[float("inf"),float('inf'),0] for j in range(k+1)] for i in range(n+1)]

for i in range(1, n - k):
    if i>1:
        dp[i][0] = min()
    elif i==1:
        dp[i][0][1] = 0
    for j in range(1, k-1):
        dp[i][j] = min(dp[i-1][j-1], max(l[i - 1], dp[i - 1][j - 1]))