n,m=map(int,input().split(' '))
dp=[[0 for i in range(m)] for j in range(n)]
table=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    table[i]=list(map(int,input().split()))

    if i>0:
        dp[i][0]=table[i][0]+dp[i-1][0]
    else:
        dp[0][0]=table[0][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + table[0][j]
for i in range(1,n):
    for j in range(1,m):
        dp[i][j]=table[i][j]+min(dp[i-1][j],dp[i][j-1])
print(dp[n-1][m-1])
