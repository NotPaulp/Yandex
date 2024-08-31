import math
import sys

sys.setrecursionlimit(10**5)
def find_round(x, y, p, enemySoldiers, round):
    if x <= 0:
        return float('inf')
    elif y <= 0 + enemySoldiers <= 0:
        return round
    else:
        if x >= y and ((y + enemySoldiers) / x < (1 + math.sqrt(5)) / 2):
            x1 = x
            y1 = y
            enemySoldiers1 = enemySoldiers
            if enemySoldiers1 >= x1:
                enemySoldiers1 -= x1 - 1
                attack = 1
            else:
                attack = x1 - enemySoldiers1
                enemySoldiers1= 0
            y1 -= attack
            x1 -= enemySoldiers1
            if y1 > 0:
                enemySoldiers1 += p
            round1 = find_round(x1, y1, p, enemySoldiers1, round + 1)

            enemySoldiers = enemySoldiers - (x - y)
            while enemySoldiers > 0:
                x -= enemySoldiers
                enemySoldiers -= x
                round += 1
            else:
                return min(round, round1)
        if enemySoldiers >= x:
            enemySoldiers -= x - 1
            attack = 1
        else:
            attack = x - enemySoldiers
            enemySoldiers = 0
        y -= attack
        x -= enemySoldiers
        if y > 0:
            enemySoldiers += p
        round += 1
        return find_round(x, y, p, enemySoldiers, round)
x = int(input())
y = int(input())
p = int(input())
enemySoldiers = 0
round = 1
answer = find_round(x, y, p, enemySoldiers, round)
if answer < float('inf'): print(answer)
else: print(-1)


