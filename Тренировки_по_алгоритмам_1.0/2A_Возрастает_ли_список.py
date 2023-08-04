list1=list(map(int,input().split(' ')))
for i in range(1,len(list1)):
    if list1[i-1]>=list1[i]:
        print("NO")
        break
else:
    print("YES")
