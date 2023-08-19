n,k=map(int,input().split())
string=input()
L=R=0
subL=0
length=1
substring={string[0]:1}
while R+1<n:
    R+=1
    new_symbol=string[R]
    substring[new_symbol]=substring.get(new_symbol,0)+1
    while substring[new_symbol]>k:
        deleted_symbol = string[L]
        substring[deleted_symbol] = substring.get(deleted_symbol, 0) - 1
        L+=1
    if R-L+1>length:
        length=R-L+1
        subL=L
print(length,subL+1)