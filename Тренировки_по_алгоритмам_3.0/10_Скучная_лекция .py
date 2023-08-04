word=input()
letters={}
for i in range(len(word)):
    letter=word[i]
    letters[ord(letter)]=letters.get(ord(letter),0)+(i+1)*(len(word)-i)
for i in range(ord('a'),ord('z')+1):
    value=letters.get(i,0)
    if value:
        print(chr(i),value,sep=': ')