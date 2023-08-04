def binary_search(m, n):
    left = 0
    right = len(m) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2

        if m[mid] >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result
M=int(input())
N=int(input())
m1=[]
m2=[]
index=0
for i in range(N):
    start,finish=map(int,input().split(' '))
    index = binary_search(m1, start)
    while True:
        while index!=None:
            start_i=m1[index]
            if start_i<=finish:
                del m1[index]
                del m2[index]
            else:
                break
            index=binary_search(m1, start)
        if len(m1)>0:
            if index==None:
                index=len(m1)-1
            elif index>0:
                index-=1
            else:
               break
            finish_i=m2[index]
            if finish_i>=start:
                del m1[index]
                del m2[index]
            else:
                index+=1
            break
        else:
            index=0
            break
    m1.insert(index,start)
    m2.insert(index, finish)
print(len(m1))