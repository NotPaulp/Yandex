import math
N=int(input())
array=list(map(int,input().split(' ')))
x=int(input())
min_difference=float('inf')
closest_number=0
for y in array:
	difference=math.fabs(y-x)
	if difference<min_difference:
		closest_number=y
		min_difference=difference
print(closest_number)