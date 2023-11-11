n=int(input())
m=int(input())
t=int(input())
l=0
r=min(n,m)//2
answer=0
while l<=r:
    width=(l+r)//2
    if width*n*2+width*m*2-width*width*4<=t:
        answer=width
        l=width+1
    else:
        r=width-1
print(answer)