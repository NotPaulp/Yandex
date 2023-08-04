n=int(input())
dp=[0]*(n+1)
solution=[]
answer=[]
current=1
for i in range(2,n+1):
    dp[i]=dp[i - 1]+1
    last=i-1
    if i%2==0:
        if dp[i]>dp[i//2]+1:
            dp[i]=dp[i//2]+1
            last = i//2
    if i % 3 == 0:
        if dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            last = i // 3
    solution.append(last)
print(dp[len(dp)-1])
i=n
while i>1:
    answer.append(solution[i-2])
    i=solution[i-2]
for i in range(len(answer)-1,-1,-1):
    print(answer[i],end=' ')
print(n,end='')
