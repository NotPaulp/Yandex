n, k, d = map(int, input().split())
profit = n
for addedDigit in range(10):
    profit = int(str(n) + str(addedDigit))
    if profit % k == 0:
        print(str(profit) + '0' * (d - 1))
        break
else:
    print(-1)
