n=int(input())
dp=[0,0,1]
for i in range(3,n+1+3):
    dp.append(2*dp[i-1]-dp[i-4])
print(dp[len(dp)-1])
