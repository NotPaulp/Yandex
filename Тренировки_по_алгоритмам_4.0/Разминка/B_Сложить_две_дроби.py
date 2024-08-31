def NOD(x, y):
    while x * y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


a, b, c, d = map(int, input().split())
x , y = a * d + b * c, b * d
nod = NOD(x, y)
x//=nod
y//=nod
print(x, y)
