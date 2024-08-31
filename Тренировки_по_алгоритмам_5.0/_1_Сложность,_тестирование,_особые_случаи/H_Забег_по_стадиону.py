import math

L, x1, v1, x2, v2 = map(int, input().split())
# if x1 == x2 or L - x1 == x2:
#     print("YES")
#     print(0)
# elif x1 > x2 and v1 != v2:
#     print("YES")
#     print(math.fabs((x2 - x1) / (v1 - v2)))
# else:
#     if v1 + v2 != 0:
#         print("YES")
#         print((L - x1 - x2) / math.fabs(v1 + v2))
#     else:
#         print("NO")
if v1 == v2:
    if v1 != 0:
        print("YES")
        print(math.fabs(L - x1 - x2) / (v1 + v2))
    elif x1 == x2:
        print("YES")
        print(0)
    else:
        print("NO")
else:
    print(min(math.fabs((x2 - x1)/(v1 - v2)),(math.fabs(L - x1 - x2)/(v1 + v2))))
# print(math.fabs((x2 - x1) / (v1 - v2)))
# print((L - x1 - x2) / (v1 + v2))
# print(math.fabs((x2 + x1) / (v1 + v2)))