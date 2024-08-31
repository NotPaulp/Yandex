# n=int(input())
# m=int(input())
# c2=int(input())
# c5=int(input())
# dp=[[0,float('inf')] for i in range(m+1)]
# dp[0]=[n,min(c2,c5)*int(n<m)]
# for i in range(len(dp)):
#
# print(dp[])
import math

n=int(input())
m=int(input())
c2=int(input())
c5=int(input())
c2_value=c2
c5_value=c5/4
cost=0
if m<=n:
    cost=0
elif c5_value<=c2_value:
    cost=c5 * ((m-n)//4)
    rest=(m-n)%4
    cost+=min(rest*c2,c5)
else:
    cost=c2*(m-n)
print(cost)


