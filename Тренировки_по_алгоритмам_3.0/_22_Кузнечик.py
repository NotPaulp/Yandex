n,k=map(int,input().split(' '))
dp=[0]*k+[1]
for i in range(len(dp),n+len(dp)-1):
    dp_i=0
    for j in range(1,k+1):
        dp_i+=dp[i-j]
    dp.append(dp_i)
print(dp[len(dp)-1])