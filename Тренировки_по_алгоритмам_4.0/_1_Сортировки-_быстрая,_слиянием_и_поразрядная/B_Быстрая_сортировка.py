import random

def partition(list1,x):
    equal=-1
    greater=-1
    for new in range(len(list1)):
        if list1[new] < x:
            if equal != -1 and greater != -1:
                list1[equal],list1[greater],list1[new]=list1[new],list1[equal],list1[greater]
                equal+=1
                greater+=1
            elif equal != -1 and greater == -1:
                list1[equal], list1[new] = list1[new], list1[equal]
                equal+=1
            elif equal == -1 and greater != -1:
                list1[greater], list1[new] = list1[new], list1[greater]
                greater+=1
        elif list1[new]==x:
            if equal!=-1 and greater!=-1:
                list1[greater],list1[new]=list1[new],list1[greater]
                greater+=1
            elif equal==-1 and greater!=-1:
                list1[greater],list1[new]=list1[new],list1[greater]
                equal=greater
                greater+=1
            elif equal==-1 and greater==-1:
                equal=new
        else:
            if greater==-1:
                greater=new
    return list1,equal,greater

def quicksort(list1):
    if len(list1)<2:
        return list1
    elif len(list1)==2:
        return [min(list1),max(list1)]
    x=random.choice(list1)
    list1,first_equal,first_greater=partition(list1,x)
    if first_greater==-1:
        return quicksort(list1[:first_equal])+list1[first_equal:]
    else:
        return quicksort(list1[:first_equal])+list1[first_equal:first_greater]+quicksort(list1[first_greater:])

n=int(input())
a=list(map(int,input().split()))
print(*quicksort(a))