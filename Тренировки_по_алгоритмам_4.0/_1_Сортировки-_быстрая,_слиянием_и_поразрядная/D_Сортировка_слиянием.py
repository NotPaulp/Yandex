def merge(list1_len,list2_len,list1,list2):
    i=0
    j=0
    combined_list=[0]*(list1_len+list2_len)
    while list1_len>i and list2_len>j:
        if list1[i]>list2[j]:
            combined_list[i+j]=list2[j]
            j+=1
        else:
            combined_list[i+j]=list1[i]
            i+=1
    if i+j<list1_len+list2_len:
        if j==list2_len:
            combined_list[(i+j):]=list1[(i):]
        if i==list1_len:
            combined_list[(i+j):]=list2[(j):]
    return combined_list
def merge_sort(sublist1,sublist2):
    len1=len(sublist1)
    len2=len(sublist2)
    if len1 > 1:
        sublist1=merge_sort(sublist1[:len1//2],sublist1[len1//2:])
    if len2 > 1:
        sublist2=merge_sort(sublist2[:len2 // 2], sublist2[len2 // 2:])
    return merge(len1,len2,sublist1,sublist2)

N=int(input())
a=list(map(int,input().split()))
print(*merge_sort(a[:N//2],a[N//2:]))
