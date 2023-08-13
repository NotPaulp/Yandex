import sys
text=sys.stdin.read()
words={}
text=text.replace('\n',' ')
text=text.strip().split(' ')
for word in text:
    if word=='':
        break
    word_count=words.get(word,0)
    print(word_count,end=' ')
    words[word]=word_count+1