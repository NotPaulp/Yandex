n,k=map(int,input().split())
cards=list(map(int,input().split()))
dict={}
for card in cards:
    dict[card]=dict.get(card,0)+1
cards=sorted(dict)
R=0
variations=0
same_cards=0
for L in range(len(cards)):
    while R<len(cards) and cards[R]<=k*cards[L]:
        if dict[cards[R]]>=2:
            same_cards+=1
        R+=1
    variations+=(R-L-1)*(R-L-2)*3
    if dict[cards[L]]>=2:
        variations+=(R-L-1)*3
        same_cards-=1
    if dict[cards[L]]>=3:
        variations+=1
    variations+=same_cards*3
print(variations)

