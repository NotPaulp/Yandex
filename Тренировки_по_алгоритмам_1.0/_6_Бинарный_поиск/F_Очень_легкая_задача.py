N,x,y=map(int,input().split())
l=0
r=(N-1)*min(x,y)
answer=r
while l<=r:
    t=(l+r)//2
    if t//x +t//y>=N-1:
        answer=t
        r=t-1
    else:
        l=t+1
answer+=min(x,y)
print(answer)