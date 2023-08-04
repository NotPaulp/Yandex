import sys
text=''
while True:
    line=input()
    if line=='':
        break
    text=text+line+' '
k=0
splits=(';','.',',','!','?','\n')
for i in splits:
    new_text=text.replace(i,' ')
    if new_text!=text:
        k+=1
        text=new_text
text=text.strip().split()

print(len(set(text))+k+1)