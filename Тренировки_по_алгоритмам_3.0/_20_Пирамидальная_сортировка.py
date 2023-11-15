class Heapmin:
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
        while i>0 and self.heap[i]<self.heap[self.parent(i)]:
            self.swap(i,self.parent(i))
            i=self.parent(i)
    def delete_min(self):
        if len(self.heap)>0:
            self.swap(0, len(self.heap)-1)
            minimum=self.heap.pop()
            self.heapify_down(0)
            return minimum
    def heapify_down(self,i):
        right=self.right_child(i)
        left=self.left_child(i)
        if right!=None and left!=None:
            if self.heap[right]>=self.heap[left]:
                min_child=left
            else:
                min_child = right
            if self.heap[i]>self.heap[min_child]:
                self.swap(i,min_child)
                self.heapify_down(min_child)
        elif left!=None:
            if self.heap[i]>self.heap[left]:
                self.swap(i,left)
                self.heapify_down(left)
    def show(self):
        print(self.heap)
heap=Heapmin()
n=int(input())
m=list(map(int,input().split(' ')))
for i in range(len(m)):
    heap.insert(m[i])
m=[]
for i in range(n):
    if i<n-1:
        print(heap.delete_min(),end=' ')
    else:
        print(heap.delete_min(),end='')