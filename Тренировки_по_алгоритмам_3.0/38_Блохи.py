def BFS(way,checked,start):
    way[0].append(start)
    checked[finish]=0
    step=0
    while step<len(way) and len(way[step])!=0:
        for vi in way[step]:
            i,j=map(int,vi.strip().split(' '))
            for i_add in range(1, 3):
                j_add = 3 - i_add
                if i + i_add <= N and j + j_add <= M:
                    vi_next=str(i + i_add) + ' ' + str(j + j_add)
                    if checked[vi_next] == -1:
                        way[step + 1].append(vi_next)
                        checked[vi_next] = checked[vi] + 1
                if i - i_add >= 1 and j + j_add <= M:
                    vi_next=str(i - i_add) + ' ' + str(j + j_add)
                    if checked[vi_next] == -1:
                        way[step + 1].append(vi_next)
                        checked[vi_next] = checked[vi] + 1
                if i + i_add <= N and j - j_add >= 1:
                    vi_next=str(i + i_add) + ' ' + str(j - j_add)
                    if checked[vi_next] == -1:
                        way[step + 1].append(vi_next)
                        checked[vi_next] = checked[vi] + 1
                if i - i_add >= 1 and j - j_add >= 1:
                    vi_next=str(i - i_add) + ' ' + str(j - j_add)
                    if checked[vi_next] == -1:
                        way[step + 1].append(vi_next)
                        checked[vi_next] = checked[vi] + 1
        step+=1


    return checked
N, M, S, T, Q=map(int,input().strip().split(' '))
finish=str(S)+' '+str(T)
ticks=[]
way = {}
checked = {}

for i in range(1,N+1):
    for j in range(1,M+1):
        way[(i - 1) * M + j - 1] = list()
        checked[str(i) + ' ' + str(j)] = -1
sum_way=0
BFS(way,checked,finish)
for i in range(Q):
    Y,X=map(int, input().strip().split())
    tick=(str(Y)+' '+str(X))
    tick_way = checked[tick]
    if tick_way == -1:
        sum_way=-1
    elif sum_way!=-1:
        sum_way += tick_way
print(sum_way)