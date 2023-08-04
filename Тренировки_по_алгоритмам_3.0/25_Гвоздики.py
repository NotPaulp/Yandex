n=int(input())
nails=list(map(int,input().strip().split(' ')))
nails=sorted(nails)
dp=[0]*n
dp[0]=0
dp[1]=nails[1]-nails[0]
if n>2:
    dp[2]=nails[2]-nails[1]+dp[1]
for i in range(3,n):
    dp[i]=min(dp[i-1]+nails[i]-nails[i-1],dp[i-2]+nails[i]-nails[i-1])
print((dp[-1]))