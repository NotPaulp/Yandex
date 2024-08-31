P, V = map(int, input().split())
Q, M = map(int, input().split())
R1, L1 = P + V, P - V
R2, L2 = Q + M, Q - M
union = 0
if R2 >= L1 and L2 <= R1:
    union = min(R2, R1) - max(L2, L1) + 1
print(R2 - L2 + 1 + R1 - L1 + 1 - union)

