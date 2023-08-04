string1=input()
string2=input()
set2=set([string2[i:i+2] for i in range(len(string2)-1)])
k=0
for i in range(len(string1)-1):
    if string1[i:i+2] in set2:
        k+=1
print(k)