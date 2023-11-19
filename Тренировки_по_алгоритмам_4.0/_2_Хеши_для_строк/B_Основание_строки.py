def pref_is_equal_suf(length, n, pref_hash, x):
    p = 10 ** 9 + 7
    return (pref_hash[length] + pref_hash[n - length] * x[length]) % p \
           == pref_hash[n]

def calculate_pref_hash_and_x(S):
    pref_hash = {}
    x = {}
    x0 = 100
    p = 10 ** 9 + 7
    x[0] = 1
    pref_hash[0] = 0
    for i in range(1, len(S)):
        x[i] = (x[i - 1] * x0) % p
        pref_hash[i] = (pref_hash[i - 1] * x0 + ord(S[i])) % p
    return pref_hash, x


prefix = " " + input()
n=len(prefix)-1
pref_hash, x = calculate_pref_hash_and_x(prefix)

for i in range(n-1, -1, -1):
    if pref_is_equal_suf(i,n,pref_hash,x):
        print(n-i)
        break