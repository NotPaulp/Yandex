N=int(input())
turtles=set()
for i in range(N):
    a,b=map(int,input().split(' '))
    ab=(a,b)
    if a>=0 and b>=0 and not(ab in turtles) and (a+b)==N-1:
        turtles.add(ab)
print(len(turtles))