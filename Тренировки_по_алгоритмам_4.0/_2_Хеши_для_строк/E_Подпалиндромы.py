def is_palindrome(center, length, pref_hash, x, suf_hash):
    p = 10 ** 18 + 7
    return (pref_hash[center] + suf_hash[center + length] * x[length]) % p \
           == (suf_hash[center] + pref_hash[center - length] * x[length]) % p


def calculate_pref_hash_and_x(S):
    pref_hash = [0] * (len(S))
    x = [0] * (len(S))
    x0 = 100
    p = 10 ** 18 + 7
    x[0] = 1
    pref_hash[0] = 0
    for i in range(1, len(S)):
        x[i] = (x[i - 1] * x0) % p
        pref_hash[i] = (pref_hash[i - 1] * x0 + ord(S[i])) % p
    return pref_hash, x


def calculate_suf_hash(S):
    suf_hash = [0] * (len(S) + 1)
    x0 = 100
    p = 10 ** 18 + 7
    suf_hash[len(S)] = 0
    for i in range(len(S) - 1, 0, -1):
        suf_hash[i] = (suf_hash[i + 1] * x0 + ord(S[i])) % p
    return suf_hash


S = ' ' + '#' + '#'.join(input()) + "#"
N = len(S)
pref_hash, x = calculate_pref_hash_and_x(S)
suf_hash = calculate_suf_hash(S)
count = 0
for center in range(1, N - 1):
    L = 2
    R = min(center - 0, N - center - 1) + 1
    maxlen = 0
    while L <= R:
        length = (L + R) // 2
        if is_palindrome(center, length, pref_hash, x, suf_hash):
            maxlen = length
            L = length + 1
        else:
            R = length - 1
    count += maxlen // 2
print(count)
