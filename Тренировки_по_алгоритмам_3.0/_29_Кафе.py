n=int(input())
dp=[[[float('inf'),True] for j in range(n+2)]for i in range(n)]
cost=[0]*n
max_cupons=0
if n>0:
    cost[0]=int(input())
    if cost[0]>100:
        dp[0][1][0]=cost[0]
        max_cupons+=1
    else:
        dp[0][0][0] = cost[0]
for i in range(1,n):
    cost[i]=int(input())
    if cost[i]<=100 and dp[i - 1][0][0] + cost[i] <= dp[i - 1][1][0]:
        dp[i][0][0] = dp[i - 1][0][0] + cost[i]
    else:
        dp[i][0][0] = dp[i - 1][1][0]
        dp[i][0][1] = False
    for j in range(1,max_cupons+2):
        if cost[i]>100:
            if dp[i-1][j-1][0]+cost[i]<=dp[i-1][j+1][0]:
                dp[i][j][0]=dp[i-1][j-1][0]+cost[i]
            else:
                dp[i][j][0] = dp[i-1][j+1][0]
                dp[i][j][1]=False
        else:
            if dp[i - 1][j][0] + cost[i]<=dp[i-1][j+1][0]:
                dp[i][j][0]=dp[i-1][j][0]+cost[i]
            else:
                dp[i][j][0] = dp[i-1][j+1][0]
                dp[i][j][1]=False
    if cost[i]>100:
        max_cupons+=1
min_cost=float('inf')
min_j=0
days=[]
if n>0:
    for j in range(len(dp[-1])):
        if dp[-1][j][0]<=min_cost:
            min_cost=dp[-1][j][0]
            min_j=j
k1=min_j
for i in range(len(dp)-1,0,-1):
    if not(dp[i][min_j][1]):
        days.append(i+1)
        min_j+=1
    else:
        if cost[i]>100:
            min_j-=1
if n>0:
    # for i in dp:
    #     print(*i)
    print(min_cost)
    k2=len(days)
    print(k1,k2)
    for i in days[::-1]:
        print(i)
else:
    print(0)
    print(0,0)
