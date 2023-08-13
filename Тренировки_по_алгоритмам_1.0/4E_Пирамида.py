n=int(input())
blocks={}
height=0
for i in range(n):
    block=tuple(map(int,input().split()))
    block_i=blocks.get(block[0],0)
    if block_i<block[1]:
        blocks[block[0]]=block[1]
        height=height-block_i+block[1]
print(height)