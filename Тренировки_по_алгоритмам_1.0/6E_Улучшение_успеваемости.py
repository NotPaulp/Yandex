from decimal import Decimal,getcontext
a=int(input())
b=int(input())
c=int(input())
getcontext().prec=max(len(str(max(a,b,c)))+1,17)
abc=a*2+b*3+c*4
l=0
r=a+b+c
answer=r
while l<=r:
    d = (l+r) // 2
    if Decimal((abc+d*5))/Decimal((a+b+c+d))>=3.5:
        answer=d
        r=d-1
    else:
        l=d+1
print(answer)
