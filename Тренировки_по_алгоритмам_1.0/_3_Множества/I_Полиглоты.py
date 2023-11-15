N=int(input())
common=set()

other=set()
for i in range(N):
    M=int(input())
    languages_i = set()
    for j in range(M):
        languages_i.add(input())
    other.update(languages_i)
    if not(i):
        common=languages_i.copy()
    common.intersection_update(languages_i)
print(len(common))
for i in common:
    print(i)
print(len(other))
for i in other:
    print(i)