n=int(input())
s1=input().strip().split(' ')
m=int(input())
s2=input().strip().split(' ')
dp=[[0 for k in range(m)] for l in range(n)]
for i in range(n):
    if i>0:
        dp[i][0]=max(int(s1[i]==s2[0]),dp[i-1][0])
    else:
        dp[i][0] = int(s1[i]==s2[0])

    for j in range(1,m):
        if i>0:
            if s1[i]==s2[j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        else:
                dp[0][j] = max(dp[0][j - 1], int(s1[0]==s2[j]))
i=n-1
j=m-1
answer=[]
while dp[i][j]>0:
    if i==0 and j==0:
        answer.append(s1[i])
        break
    elif i==0:
        if dp[i][j-1]+1==dp[i][j]:
            answer.append(s1[i])
        j-=1
    elif j==0:
        if dp[i-1][j]+1==dp[i][j]:
            answer.append(s1[i])
        i-=1
    else:
        if dp[i-1][j]>dp[i-1][j-1]:
            i-=1
        elif dp[i][j-1]>dp[i-1][j-1]:
            j-=1
        else:
            if dp[i-1][j-1]+1==dp[i][j]:
                answer.append(s1[i])
            i-=1
            j-=1
s=''
for i in range(len(answer)-1,0,-1):
    s=s+answer[i]+' '
if len(answer):
    s=s+answer[0]
print(s)
