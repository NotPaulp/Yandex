n,m=map(int,input().split(' '))
dp=[[0 for i in range(m)] for j in range(n)]
table=[[0 for i in range(m)] for j in range(n)]
way=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    table[i] = list(map(int, input().split()))
    for j in range(m):
        if i>0 and j>0:
            if dp[i-1][j]>dp[i][j-1]:
                dp[i][j]=table[i][j]+dp[i-1][j]
                way[i][j]='D'
            else:
                dp[i][j] = table[i][j] + dp[i][j - 1]
                way[i][j]='R'
        elif i>0:
            dp[i][j] = table[i][j] + dp[i - 1][j]
            way[i][j]='D'
        elif j>0:
            dp[i][j] = table[i][j] + dp[i][j - 1]
            way[i][j]='R'
        else:
            dp[0][0]=table[0][0]
            way[0][0]=None
i=n-1
j=m-1
'''
4 4
1 1 0 0
0 1 1 1
0 0 0 1
0 0 0 1
'''
answer=[]
while way[i][j]!=None:
    k=way[i][j]
    if way[i][j]=='R':
        answer.append('R')
        j-=1
    else:
        answer.append('D')
        i-=1
print(dp[n-1][m-1])
print(*answer[::-1])
