def format(number):
    number_new=''
    for symbol in number:
        if symbol.isdigit():
            number_new=number_new+symbol
    if len(number_new)==7:
        number_new='8495'+number_new
    else:
        number_new = '8' + number_new[1:]
    return number_new
number_add=format(input())
for i in range(3):
    number=format(input())
    if number==number_add:
        print("YES")
    else:
        print("NO")
