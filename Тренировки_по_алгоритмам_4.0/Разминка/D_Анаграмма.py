str1 = input()
str2 = input()
str1_symbols = {}
str2_symbols = {}
for symbol in str1:
    str1_symbols[symbol] = str1_symbols.get(symbol, 0) + 1
for symbol in str2:
    str2_symbols[symbol] = str2_symbols.get(symbol, 0) + 1
if str1_symbols==str2_symbols:
    print("YES")
else:
    print("NO")
