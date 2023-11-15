def quickselect(m,k):
    x=m[len(m)//2]
    lesser=[i for i in m if i<x]
    equal = [i for i in m if i == x]
    greater = [i for i in m if i > x]
    if k<=len(lesser):
        return quickselect(lesser,k)
    elif k<=len(lesser+equal):
        return x
    else:
        return quickselect(greater,k-len(lesser+equal))
list1=list(map(int,input(' ').strip().split()))
maxs=[0]*3
mins=[0]*2
positive=1
negative=1
for i in range(len(maxs)):
    maxs[i]=quickselect(list1,len(list1)-i)
    positive*=maxs[i]
for i in range(len(mins)):
    mins[i] = quickselect(list1,  i + 1)
    negative *= mins[i]
negative*=maxs[0]
if positive>=negative:
    print(*maxs)
else:
    print(maxs[0],*mins[::-1])




