def binary_search(n,array):
    l=0
    r=len(array)-1
    while l<=r:
        m=(l+r)//2
        if array[m]==n:
            return 'YES'
        elif n>array[m]:
            l=m+1
        else:
            r=m-1
    return "NO"
N,K=map(int,input().split())
array=list(map(int,input().split()))
numbers=list(map(int,input().split()))
for number in numbers:
    print(binary_search(number,array))
