import sys
purchases={}
text=sys.stdin.read()
text=text.replace('\n',' ')
text=text.strip().split(' ')
try:
    for i in range(0,len(text),3):
        key=text[i]+' '+text[i+1]
        amount=int(text[i+2])
        purchases[key]=purchases.get(key,0)+amount
    purchases_list=sorted(purchases.items())
    name=''
    for purchase in purchases_list:
        name_i,product_i=purchase[0].split()
        amount_i=purchase[1]
        if name!=name_i:
            name=name_i
            print(name+':')
        print(product_i,amount_i)
except IndexError:
    pass
