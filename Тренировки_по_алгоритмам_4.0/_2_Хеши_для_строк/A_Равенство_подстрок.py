def compare_substrings(start1, start2, length, pref_hash, x):
    p = 10 ** 9 + 7
    return (pref_hash[start1 + length - 1] + pref_hash[start2 - 1] * x[length]) % p \
           == (pref_hash[start2 + length - 1] + pref_hash[start1 - 1] * x[length]) % p

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

S = " "+input()
Q = int(input())
pref_hash, x = calculate_pref_hash_and_x(S)
for request in range(Q):
    L, A, B = map(int, input().strip().split())
    if compare_substrings(A+1, B+1, L, pref_hash, x):
        print('yes')
    else:
        print('no')
