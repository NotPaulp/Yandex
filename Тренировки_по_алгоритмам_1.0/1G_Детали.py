N, K, M=map(int,input().split(' '))
detali=0
while N>=K:
    zagotovki=N//K
    N=N%K
    detali+=(K//M)*zagotovki
    N+=(K%M)*zagotovki
print(detali)
