n,m=map(int,input().split(' '))
dp=[[0 for i in range(m)] for j in range(n)]
dp[0][0]=1
for i in range(1,n):
    for j in range(1,m):
        if j>=2:
            dp[i][j]+=dp[i-1][j-2]
        if i>=2:
            dp[i][j]+=dp[i-2][j-1]
print(dp[n-1][m-1])