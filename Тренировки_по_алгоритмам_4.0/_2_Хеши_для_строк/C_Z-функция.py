def z(S):
    z_arr = [0] * len(S)
    z_arr[0] = 0
    l = r = 0
    for i in range(1, len(S)):
        if i <= r:
            z_arr[i] = min(z_arr[i - l], r - i + 1)
        while i + z_arr[i] < len(S):
            if (S[i + z_arr[i]] == S[z_arr[i]]):
                z_arr[i] += 1
            else:
                break
        if (z_arr[i] > 0 and i + z_arr[i] - 1 > r):
            l = i
            r = i + z_arr[i] - 1
    return z_arr

S = input()
print(*z(S))
