n=int(input())
a=list(map(int,input().split(' ')))
stack=[]
answer={}
for i in range(len(a)):
    while stack and a[i]<stack[len(stack)-1][1]:
        prev=stack.pop()
        answer[prev[0]]=i
    stack.append([i,a[i]])
while stack:
    prev = stack.pop()
    answer[prev[0]] = -1
for i in range(len(answer)):
    if i!=(len(a)-1):
        print(answer[i],end=' ')
    else:
        print(answer[i],end='')