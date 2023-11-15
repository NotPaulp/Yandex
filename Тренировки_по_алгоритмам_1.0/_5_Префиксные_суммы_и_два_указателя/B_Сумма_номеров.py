N,K=map(int,input().split())
cars=list(map(int,input().split()))
prefsum=[0]*(N+1)
prefsum[0]=0
prefsum[1]=cars[0]
count=0
numbers={0}
for i in range(1,N+1):
    prefsum[i]=prefsum[i-1]+cars[i-1]
    if prefsum[i]>=K:
        value=prefsum[i]-K
        if value in numbers:
            count+=1
    numbers.add(prefsum[i])
print(count)