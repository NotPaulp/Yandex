N,W=map(int,input().split(' '))
workers=[]
time_ranges=[]
for i in range(N):
    start,finish=map(int,input().split(' '))
    finish+=start
    time_ranges.append([start,finish])
time_ranges=sorted(time_ranges,key=lambda x:x[0])
for time_range in time_ranges:
    for i in range(len(workers)):
        if workers[i][-1][1]<=time_range[0]:
            workers[i].append(time_range)
            break
    else:
        workers.append([time_range])
print(len(workers))
for worker in workers:
    for time_range in worker:
        print(time_range[0],end=' ')
