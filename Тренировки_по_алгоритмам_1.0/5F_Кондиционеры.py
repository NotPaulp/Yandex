n=int(input())
a=list(map(int,input().strip().split()))
m=int(input())
max_power=0
bc={}
for j in range(m):
    bc_j=list(map(int,input().split()))
    if bc_j[1]<bc.get(bc_j[0],float('inf')):
        bc[bc_j[0]]=bc_j[1]
    max_power=max(max_power,bc_j[0])
pref_min=[float('inf')]*(max_power+1)
pref_min[max_power]=bc.get(max_power)
for power in range(max_power-1,0,-1):
    pref_min[power]=min(pref_min[power+1],bc.get(power,float('inf')))
cost=0
for ai in a:
    cost+=pref_min[ai]
print(cost)