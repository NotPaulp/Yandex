n=int(input())
emphases={}
errors=0
for i in range(n):
    word=input()
    word_lower=word.lower()
    emphases[word_lower]=emphases.get(word_lower,set())
    emphases[word_lower].add(word)
text=input().split()
for word in text:
    word_lower = word.lower()
    if emphases.get(word_lower,False):
        if not(word in emphases[word_lower]):
            errors+=1
    else:
        upper_cases=0
        for letter in word:
            if letter.isupper():
                upper_cases+=1
                if upper_cases>1:
                    break
        if upper_cases!=1:
            errors+=1
print(errors)