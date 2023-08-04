N=int(input())
K=int(input())
Row=int(input())
Column=int(input())
Seat=(Row*2-int(Column==1))
if Seat%K==0:
    Var=K
else:
    Var =Seat% K
before=[float('-inf'),1]
after=[float('inf'),1]
if Seat+K<=N:
    after=[(Seat+K+1)//2,2-(Seat+K)%2]

if Seat - K > 0:
    before=[(Seat-K+1)//2,2-(Seat-K)%2]
if after[0]-Row<=Row-before[0]:
    answer=after
else:
    answer=before
if answer[0]!=float('inf'):
    print(*answer)
else:
    print(-1)
