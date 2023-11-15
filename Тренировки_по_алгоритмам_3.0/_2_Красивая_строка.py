k=int(input())
s=input()
chrs=[]
maxlen=0

for n in range(ord('a'),ord('z')+1):
    char=chr(n)
    strlen = 0
    last_j = 0
    kcopy = k
    stop = False
    for i in range(0,len(s)):
        if s[i-1]!=char and i>0:
            if kcopy < k:
                kcopy += 1
        if strlen>0:
            strlen-=1
        for j in range(max(last_j,i),len(s)):
            if s[j]!=char:
                if kcopy>0:
                    kcopy-=1
                else:
                    last_j=j
                    break
            strlen+=1
            if j==len(s)-1:
                stop=True
                break
        if strlen>maxlen:
            maxlen=strlen
        if stop:
            break
print(maxlen)