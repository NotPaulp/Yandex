n=int(input())
synonyms={}
for i in range(n):
    words=input().split(' ')
    synonyms[words[0]] = words[1]
    synonyms[words[1]] = words[0]
print(synonyms[input()])