N=int(input())
numbers=list(map(int,input().strip().split(' ')))
numbers_reversed=numbers[::-1]
pref_function=[0]*len(numbers)
pref_function[0]=int(numbers[0]==numbers_reversed[0])
for i in range(1,N):
    k=pref_function[i-1]
    while numbers[i]!=numbers_reversed[k] and k>0:
            k=pref_function[k-1]
    if numbers[i]==numbers_reversed[k]:
        k+=1
    pref_function[i] = k
M=N-pref_function[-1]
print(M)
if M:
    print(*numbers_reversed[pref_function[-1]:])
