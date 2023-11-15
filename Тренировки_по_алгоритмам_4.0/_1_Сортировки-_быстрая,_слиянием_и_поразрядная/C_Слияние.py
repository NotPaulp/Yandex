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
if __name__ == "__main__":
    N=int(input())
    a=list(map(int,input().split()))
    M=int(input())
    b=list(map(int,input().split()))
    print(*merge(N,M,a,b))