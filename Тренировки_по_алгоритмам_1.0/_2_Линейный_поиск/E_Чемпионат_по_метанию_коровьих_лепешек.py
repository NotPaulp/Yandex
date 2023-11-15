n = int(input())
results = list(map(int, input().split(' ')))
winners_result_index = results.index(max(results))
max_place = 1
result = 0
for i in range(winners_result_index+1, len(results) - 1):
    if results[i] > results[i + 1] and results[i] % 5 == 0 and results[i] % 2 == 1:
        if results[i] > result:
            result = results[i]
for i in results:
    if i > result:
        max_place += 1

if result != 0:
    print(max_place)
else:
    print(result)