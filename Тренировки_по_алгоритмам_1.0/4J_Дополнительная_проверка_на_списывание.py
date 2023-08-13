import sys
def is_number(string):
    for char in string:
        if not(char.isnumeric()):
            return False
    return True
n,C,D=input().split()
key_words=set()
words={}
for i in range(int(n)):
    word=input()
    if C=='no':
        word=word.lower()
    if not(is_number(word)):
        key_words.add(word)
text=sys.stdin.read()
symbols=['\n','{','}','(',')',';',',',':','.','%',"'",'"','+','-','*',
'/','=','&',"#","@",'[',']',"|",'$','^','~','<','\\','\\\\',">",'`','!',
"?"]
for symbol in symbols:
    text=text.replace(symbol,' ')
text=text.strip().split()
frequent_word=''
for word in text:
    if C=='no':
        word=word.lower()
    if not(is_number(word)) and (not(word[0].isdigit()) or D=='yes') and not(word in key_words):
        words[word]=words.get(word,0)+1
for word in words:
    if words[word]>words.get(frequent_word,0):
        frequent_word=word
print(frequent_word)
