N=int(input())
last=int(input())
answer=0
for i in range(1,N):
    current=int(input())
    answer+=min(current,last)
    last=current
print(answer)