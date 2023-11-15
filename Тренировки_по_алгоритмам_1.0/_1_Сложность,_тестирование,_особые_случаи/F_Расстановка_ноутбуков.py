a1,b1,a2,b2=map(int,input().split(' '))
a1,b1=min(a1,b1),max(a1,b1)
a2,b2=min(a2,b2),max(a2,b2)
if a1>=b2:
    print(a1,b1+a2)
elif a2>=b1:
    print(a2,b2+a1)
else:
    print(a1+a2,max(b1,b2))