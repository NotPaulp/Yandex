def neighbours(field,vi):
    if 
def BFS(field,way,finish):
    step=0
    while way.get(step,False):
        for vi in way[step]:
            if vi == finish:
                return step
            else:
                for next_vi in

way={}
H,W=map(int,input().split(' '))
checked=[[float('inf') for _ in range(W)] for _ in range(H)]
field=['' for i in range(H)]
for i in range(H):
    field[i]=input()
start=list(map(int,input()))
way[0]=list()
way[0].append(start)
finish=list(map(int,input()))
