n=int(input())
points=set()
answer=0
for i in range(n):
    points.add(tuple(map(int,input().split())))
for point1 in points:
    deltas=set()
    lens=[]
    for point2 in points:
        if point1!=point2:
            deltax=point1[0]-point2[0]
            deltay=point1[1]-point2[1]
            delta=(deltax,deltay)
            nega_delta=(-deltax,-deltay)
            d=(deltax)**2+(deltay)**2
            lens.append(d)
            if delta in deltas:
                answer-=1
            deltas.add(nega_delta)
    lens.sort()
    R=0
    for L in range(len(lens)):
        while R<len(lens) and lens[L]==lens[R]:
            R+=1
        answer+=R-L-1
print(answer)


