N=int(input())
shirts=list(map(int,input().split()))
M=int(input())
pants=list(map(int,input().split()))
shirts_pointer=0
pants_pointer=0
min_diff=float('inf')
pair=[0,0]
while shirts_pointer<N and pants_pointer<M and min_diff>0:
    if shirts[shirts_pointer]>pants[pants_pointer]:
        diff=shirts[shirts_pointer]-pants[pants_pointer]
        if diff<min_diff:
            min_diff=diff
            pair[0]=shirts[shirts_pointer]
            pair[1]=pants[pants_pointer]
        pants_pointer+=1
    elif shirts[shirts_pointer]==pants[pants_pointer]:
        min_diff=0
        pair[0] = shirts[shirts_pointer]
        pair[1] = pants[pants_pointer]
    else:
        diff=pants[pants_pointer]-shirts[shirts_pointer]
        if diff < min_diff:
            min_diff = diff
            pair[0] = shirts[shirts_pointer]
            pair[1] = pants[pants_pointer]
        shirts_pointer+=1
print(*pair)