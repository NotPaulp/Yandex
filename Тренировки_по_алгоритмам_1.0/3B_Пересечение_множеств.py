a=set(list(map(int,input().strip().split(' '))))
b=set(list(map(int,input().strip().split(' '))))
print(*sorted(a.intersection(b)))