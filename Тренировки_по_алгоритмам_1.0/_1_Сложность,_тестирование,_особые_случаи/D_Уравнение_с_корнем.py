a=int(input())
b=int(input())
c=int(input())
if c<0:
    print("NO SOLUTION")
elif a==0:
    if c**2-b==0:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    solution=(c*c-b)/a
    if int(solution)==solution:
        print(int(solution))
    else:
        print("NO SOLUTION")