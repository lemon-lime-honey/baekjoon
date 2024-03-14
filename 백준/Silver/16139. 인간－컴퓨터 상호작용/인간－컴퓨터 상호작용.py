import sys
input = sys.stdin.readline

s = input()
q = int(input())
result = list()
letters = [[0 for i in range(26)] for j in range(len(s))]
letters[0][ord(s[0]) - ord('a')] = 1

for i in range(1, len(s)):
    target = ord(s[i]) - ord('a')
    for j in range(26):
        if j != target:
            letters[i][j] = letters[i - 1][j]
        else:
            letters[i][j] = letters[i - 1][j] + 1

for i in range(q):
    a, l, r = input().rstrip().split()
    l, r = int(l), int(r)
    target = ord(a) - ord('a')
    if l == 0:
        result.append(letters[r][target])
    else:
        result.append(letters[r][target] - letters[l - 1][target])

print(*result, sep='\n')