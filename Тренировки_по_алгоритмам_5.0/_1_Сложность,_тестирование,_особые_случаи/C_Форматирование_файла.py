n = int(input())
presses = 0
for _ in range(n):
    ai = int(input())
    presses += ai // 4 + min(ai%4, -(ai%-4) + 1)
print(presses)