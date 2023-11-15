s = open("input.txt", 'r')
s = s.read()
m = {}
for i in s:
    if i != ' ' and i != '\n':
        m[ord(i)] = m.get(ord(i), 0) + 1
m = sorted(m.items(), key=lambda x: x[0], reverse=False)
u = max(m, key=lambda x: x[1])[1]
for i in range(u):
    s = ''
    for j in range(len(m)):
        if m[j][1] >= (u - i):
            s = s + '#'
        else:
            s = s + ' '
    print(s)

s = ''
for i in range(len(m)):
    s = s + chr(m[i][0])
print(s)