list1=list(map(int,input(' ').strip().split()))
max1=float('-inf')
max2=float('-inf')
min1=float('inf')
min2=float('inf')
for i in list1:
    if max1<=i:
        max2=max1
        max1=i
    elif max2<=i:
        max2=i
    if min1>=i:
        min2=min1
        min1=i
    elif min2>=i:
        min2=i
if (max1*max2>min1*min2):
    print(max2,max1)
else:
    print(min1,min2)