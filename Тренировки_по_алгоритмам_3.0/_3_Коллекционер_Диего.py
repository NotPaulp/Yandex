def count_smaller_elements(array, N, right):
    count = 0
    left = 0

    while left <= right:
        mid = (left + right) // 2
        if array[mid] < N:
            count += mid - left + 1
            left = mid + 1
        else:
            right = mid - 1

    return count
N=int(input())
stickers=list(map(int,input().split(' ')))
K=int(input())
p=list(map(int,input().split(' ')))
stickers=sorted(stickers)
stickers_new=[0]*N
stickers_new[0]=(stickers[0])
k=1
for i in range(1,N):
    if stickers[i]!=stickers[i-1]:
        stickers_new[k]=stickers[i]
        k+=1

for i in p:
    print(count_smaller_elements(stickers_new,i,k-1))