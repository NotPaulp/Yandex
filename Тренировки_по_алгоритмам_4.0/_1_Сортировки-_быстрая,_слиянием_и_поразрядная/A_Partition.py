def partition(list1,x):
    lesser=0
    greater=0
    for ai in list1:
        if ai<x:
            lesser+=1
        else:
            greater+=1
    return lesser,greater
N=int(input())
a=list(map(int,input().split()))
x=int(input())
lesser,greater=partition(a,x)
print(lesser)
print(greater)
