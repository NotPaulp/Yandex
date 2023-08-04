n=int(input())
min_border=30
max_border=4000
last=0
current=0
for i in range(n):
    if not(i):
        current=last=float(input())
    else:
        input_string=input().strip().split(' ')
        current=float(input_string[0])
        if input_string[1]=='closer':
            if current > last:
                min_border = max(last + (current - last) / 2, min_border)
            elif current < last:
                max_border = min(current + (last - current) / 2, max_border)
        else:
            if current > last:
                max_border = min(last + (current - last) / 2, max_border)
            elif current < last:
                min_border = max(current + (last - current) / 2, min_border)
        last=current
print(min_border,max_border)