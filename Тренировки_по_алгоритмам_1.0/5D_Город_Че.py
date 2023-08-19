n,r=map(int,input().strip().split())
d=list(map(int,input().strip().split()))
L=0
count=0
R=n-1
while d[R]-d[L]>r:
    count += 1
    R -= 1
R+=1
while True:
    L += 1
    while R<n and d[R]-d[L]<=r:
        R+=1
    if R>=n:
        break
    count+=n-R
print(count)