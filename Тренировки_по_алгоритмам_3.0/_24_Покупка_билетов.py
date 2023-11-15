n=int(input())
dp=[0]*(n+3)
dp_n=0
A1=3601
B1=3601
C1=3601
A2=3601
B2=3601
C2=3601
A3=3601
B3=3601
C3=3601
for i in range(3,n+3):
    A3 = A2
    B3 = B2
    C3 = C2
    A2 = A1
    B2 = B1
    C2 = C1
    A1,B1,C1=map(int,input().strip().split(' '))
    dp_n=dp[i]=min(A1+dp[i-1],B2+dp[i-2],C3+dp[i-3])
print(dp_n)