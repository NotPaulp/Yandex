import sys
text=sys.stdin.read()
words={}
frequent_word=''
max_count=0
text=text.replace('\n',' ')
text=text.strip().split(' ')
for word in text:
    if word!='':
        word_count=words.get(word,0)+1
        if word_count>max_count:
            max_count=word_count
            frequent_word=word
        elif word_count==max_count:
            if word<frequent_word:
                max_count = word_count
                frequent_word = word
        words[word]=word_count+1
print(frequent_word)
