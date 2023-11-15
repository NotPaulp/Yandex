g,S=map(int,input().split())
alphabet=input()
sequence=input()
matches=0
word={}
current_word={}
for symbol in alphabet:
    word[symbol]=word.get(symbol,0)+1
for symbol in sequence[:g]:
    current_word[symbol]=current_word.get(symbol,0)+1
    if current_word[symbol] == word.get(symbol):
        matches += 1
    elif current_word[symbol] - 1 == word.get(symbol):
        matches -= 1
first_symbol=sequence[0]
count=int(matches==len(word))
i=0
for symbol in sequence[g:]:
    i+=1

    current_word[first_symbol]=current_word[first_symbol]-1
    if current_word[first_symbol]+1==word.get(first_symbol):
        matches-=1
    elif current_word[first_symbol]==word.get(first_symbol):
        matches+=1

    current_word[symbol]=current_word.get(symbol,0)+1
    if current_word[symbol]==word.get(symbol):
        matches+=1
    elif current_word[symbol]-1==word.get(symbol):
        matches-=1

    if matches==len(word):
        count+=1
    first_symbol = sequence[i]
print(count)