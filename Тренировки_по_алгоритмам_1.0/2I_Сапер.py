N,M,K=map(int,input().strip().split(' '))
field=[[0 for j in range(M)] for i in range(N)]
shift=[-1,0,1]
for i in range(K):
    y,x=map(int,input().split(' '))
    y-=1
    x-=1
    field[y][x]='*'
    for y_add in shift:
        for x_add in shift:
            if y_add+y>-1 and x_add+x>-1 and y_add+y<N and x_add+x<M:
                if field[y+y_add][x+x_add]!='*':
                    field[y+y_add][x+x_add]+=1
for row in field:
    print(*row)