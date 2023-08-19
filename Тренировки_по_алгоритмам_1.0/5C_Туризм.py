N=int(input())
y=[0]*N
prefsum_lr=[0]*N
prefsum_rl=[0]*N
for i in range(N):
    y[i]=int(input().split()[1])
    if i>0:
        prefsum_lr[i]=prefsum_lr[i-1]+(y[i]-y[i-1])*int(y[i]>y[i-1])
for i in range(N-2,-1,-1):
    prefsum_rl[i] = prefsum_rl[i + 1] + (y[i] - y[i + 1]) * int(y[i] > y[i + 1])
M=int(input())
for i in range(M):
    start,finish=map(int,input().split())
    if finish>=start:
        print(prefsum_lr[finish-1] - prefsum_lr[start-1])
    else:
        print(prefsum_rl[finish-1] - prefsum_rl[start-1])