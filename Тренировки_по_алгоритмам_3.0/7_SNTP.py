def format(m):
    return m[0]*3600+m[1]*60+m[2]
def result(A,B,C):
    if C<A:
        C+=24*3600
    travel=int((C-A)/2)+int((((C-A)/2-int((C-A)/2))>=0.5))
    time= (travel+B)%(24*3600)
    hours=str(time//3600)
    minutes=str(time%3600//60)
    seconds=str(time%3600%60)
    hours=(2-len(hours))*'0'+hours
    minutes=(2-len(minutes))*'0'+minutes
    seconds = (2 - len(seconds)) * '0' + seconds
    print(hours,minutes ,seconds ,sep=':')
A=list(map(int,input().split(':')))
B=list(map(int,input().split(':')))
C=list(map(int,input().split(':')))
A=format(A)
B=format(B)
C=format(C)
result(A,B,C)