def DFS(v, start, checked, component):
    stack = [start]
    checked[start] = True

    while stack:
        current = stack.pop()
        component.append(current)

        for vi in v[current]:
            if not checked[vi]:
                stack.append(vi)
                checked[vi] = True


V, E = map(int, input().split())
checked = [False] * (V + 1)
v = {}
components = []
lens = []

for i in range(1, V + 1):
    v[i] = []

for i in range(E):
    f, s = map(int, input().split())
    v[f].append(s)
    v[s].append(f)

for i in range(1, V + 1):
    if not checked[i]:
        component = []
        DFS(v, i, checked, component)
        lens.append(len(component))
        components.append(component)

print(len(lens))
for i in range(len(lens)):
    print(lens[i])
    print(*components[i])