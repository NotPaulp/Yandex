n=int(input())
broken={}
for i in range(n):
    broken[i]='NO'
keys=list(map(int,input().split()))

typing=int(input())
typings=list(map(int,input().split()))
for t in typings:
    if keys[t-1]==0:
        broken[t-1]='YES'
    keys[t - 1] -= 1
for i in range(n):
    print(broken[i])