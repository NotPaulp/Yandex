n = int(input())
a = list(map(int,input().split()))
prevOdd = False
operations = ''
for ai in a:
    currentOdd = ai % 2 == 1
    if prevOdd and currentOdd:
        operations = operations + 'x'
    else:
        operations = operations + '+'
        if prevOdd or currentOdd:
            prevOdd = True
operations = operations[1:]
print(operations)
