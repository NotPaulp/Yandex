n=int(input())
day=1
prev_time=-1
for i in range(n):
    hours,minutes,seconds=map(int,input().split(':'))
    time=hours*3600+minutes*60+seconds
    if time<=prev_time:
        day+=1
    prev_time=time
print(day)
