class Heapmax:
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1)//2
    def left_child(self,i):
        return 2*i+1 if 2*i+1<len(self.heap) else None
    def right_child(self,i):
        return 2*i+2 if 2*i+2<len(self.heap) else None
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j], self.heap[i]
    def insert(self,value):
        self.heap.append(value)
        self.heapify(len(self.heap)-1)
    def heapify(self,i):
        while i>0 and self.heap[i]>self.heap[self.parent(i)]:
            self.swap(i,self.parent(i))
            i=self.parent(i)
    def delete_max(self):
        if len(self.heap)>0:
            self.swap(0, len(self.heap)-1)
            maximum=self.heap.pop()
            self.heapify_down(0)
            return maximum
    def heapify_down(self,i):
        right=self.right_child(i)
        left=self.left_child(i)
        if right!=None and left!=None:
            if self.heap[right]>=self.heap[left]:
                max_child=right
            else:
                max_child = left
            if self.heap[i]<self.heap[max_child]:
                self.swap(i,max_child)
                self.heapify_down(max_child)
        elif left!=None:
            if self.heap[i]<self.heap[left]:
                self.swap(i,left)
                self.heapify_down(left)
    def show(self):
        print(self.heap)
k,n,m=map(int,input().strip().split())
sidewalks={}
ranges=Heapmax()
ranges_sum=0
for i in range(n):
    d,w=map(int,input().strip().split())
    if w not in sidewalks:
        sidewalks[w]=[d]
    else:
        ranges.insert(d - sidewalks[w][len(sidewalks[w])-1])
        ranges_sum += d - sidewalks[w][len(sidewalks[w])-1]
        sidewalks[w].append(d)
if m<len(sidewalks):
    print(-1)
else:
    for i in range(m-len(sidewalks)):
        ranges_sum-=ranges.delete_max()
    print(ranges_sum)

