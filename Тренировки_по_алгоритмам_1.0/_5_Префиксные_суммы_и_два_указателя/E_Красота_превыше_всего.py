
N,K=map(int,input().split())
trees=list(map(int,input().strip().split()))
l=L=0
r=R=N-1
min_length=N
needed_trees=set()
dict={}

for tree in trees:
    dict[tree]=dict.get(tree,0)+1
while dict[trees[R]]>1:
    dict[trees[R]] = dict.get(trees[R], 0) - 1
    R -= 1
r=R
min_length=R-L+1
while True:
    dict[trees[L]] = dict.get(trees[L], 0) - 1
    if dict[trees[L]] <= 0:
        needed_trees.add(trees[L])
        dict[trees[L]]=0
    L += 1
    while needed_trees:
        R+=1
        if R>=N:
            break
        dict[trees[R]]=dict.get(trees[R],0)+1
        if dict[trees[R]]==1:
            needed_trees.discard(trees[R])
    if R>=N:
        break
    length=R-L+1
    if length<min_length:
        r=R
        l=L
        min_length=length
print(l+1,r+1)

