def get_lps(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0: length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def search(pattern, target):
    m = len(pattern)
    n = len(target)

    lps = [0 for i in range(m)]
    i, j = 0, 0

    get_lps(pattern, m, lps)

    while (n - i) >= (m - j):
        if pattern[j] == target[i]:
            i += 1
            j += 1
        if j == m:
            result.append(i - j + 1)
            j = lps[j - 1]
        elif i < n and pattern[j] != target[i]:
            if j != 0: j = lps[j - 1]
            else: i += 1


t = input()
p = input()

result = list()
search(p, t)

print(len(result))
if result: print(*result)
