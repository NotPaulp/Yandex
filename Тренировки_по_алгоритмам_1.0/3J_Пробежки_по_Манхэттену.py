import math
t,d,n=map(int,input().split())
possible_positions=set()
for i in range(n):
    x_y=tuple(list(map(int,input().split())))
    possible_positions_i=set()
    for x_add in range(-d,d+1):
        abs_x=int(math.fabs(x_add))
        for y_add in range(abs_x-d,d-abs_x+1):
            possible_positions_i.add()
