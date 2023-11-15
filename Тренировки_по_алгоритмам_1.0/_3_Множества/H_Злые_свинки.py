N=int(input())
birds=set()
for i in range(N):
    x,y=map(int,input().split(' '))
    if not(x in birds):
        birds.add(x)
print(len(birds))