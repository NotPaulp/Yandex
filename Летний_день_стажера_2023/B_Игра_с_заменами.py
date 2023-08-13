t=int(input())
for _ in range(t):
    dict1 = {}
    dict2={}
    s1=input()
    s2=input()
    for i in range(len(s1)):
        if dict1.get(s1[i],False) and not(dict1[s1[i]]==s2[i]):
            print('NO')
            break
        else:
            dict1[s1[i]] = s2[i]
        if dict2.get(s2[i],False) and not(dict2[s2[i]]==s1[i]):
            print('NO')
            break
        else:
            dict2[s2[i]] = s1[i]
    else:
        print('YES')