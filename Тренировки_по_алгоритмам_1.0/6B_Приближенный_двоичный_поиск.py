def binary_search_closest(n,array):
    l=0
    nclosest=-1
    r=len(array)-1
    mindiff=float("inf")
    while l<=r:
        m=round((l+r)/2)
        if array[m]==n:
            return n
        elif n>array[m]:
            if n-array[m]<mindiff:
                mindiff=n-array[m]
                nclosest=array[m]
            elif n-array[m] ==mindiff:
                nclosest=min(nclosest,array[m])
            l=m+1
        else:
            if array[m]-n<mindiff:
                mindiff=array[m]-n
                nclosest=array[m]
            elif array[m]-n==mindiff:
                nclosest = min(nclosest, array[m])
            r=m-1
    return nclosest
N,K=map(int,input().split())
array=list(map(int,input().split()))
numbers=list(map(int,input().split()))
for number in numbers:
    print(binary_search_closest(number,array))
