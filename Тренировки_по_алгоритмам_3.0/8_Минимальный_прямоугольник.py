K=int(input())
minX=float('inf')
minY=float('inf')
maxX=0
maxY=0
for i in range(K):
    X,Y=map(int,input().split(' '))
    minX=min(X,minX)
    minY=min(Y,minY)
    maxX=max(X,maxX)
    maxY=max(Y,maxY)
print(minX,minY,maxX,maxY)
