troom,tcond=map(int,input().split(' '))
command=input()
if command=='freeze':
    print(min(troom,tcond))
elif command=='heat':
    print(max(troom,tcond))
elif command=='auto':
    print(tcond)
elif command=='fan':
    print(troom)

