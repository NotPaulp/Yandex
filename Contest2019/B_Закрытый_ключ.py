x,y=map(int,input().split(' '))
max_divisor=y/x
count=0
if int(max_divisor)==max_divisor:
    for i in range(int(max_divisor)+1,x):
        quotient=y/i
        if int(quotient)==quotient:
            count+=1
            print(i,quotient)
print(count)

