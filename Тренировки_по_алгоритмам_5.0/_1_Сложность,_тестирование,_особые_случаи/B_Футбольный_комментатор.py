G1home, G2guest = map(int, input().split(":"))
G1guest, G2home = map(int, input().split(":"))
where = int(input())

if where == 2:
    G1home, G1guest = G1guest, G1home
    G2home, G2guest = G2guest, G2home

if G1home + G1guest > G2home + G2guest:
    print(0)

elif G1home + G1guest == G2home + G2guest:
    if G2guest >= G1guest:
        print(1)
    else:
        print(0)

else:
    diff = G2home + G2guest - (G1home + G1guest)
    if diff + G1guest > G2guest and (where==1 or G1guest > G2guest):
        print(diff)
    else:
        print(diff + 1)