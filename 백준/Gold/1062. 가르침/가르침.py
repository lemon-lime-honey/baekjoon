import sys
input = sys.stdin.readline


def dfs(idx, letters):
    cnt = 0

    if letters.bit_count() == k:
        for word in words:
            if letters & word == word:
                cnt += 1
        return cnt

    for i in range(idx, 26):
        if i in (0, 2, 8, 13, 19): continue
        cnt = max(cnt, dfs(i + 1, letters | (1 << i)))

    return cnt

n, k = map(int, input().split())
words = [0 for i in range(n)]

for i in range(n):
    word = input().rstrip()
    for letter in word:
        words[i] |= 1 << ord(letter) - ord('a')

if k < 5:
    print(0)
    sys.exit()

learnt = 0

for letter in 'antic':
    learnt |= 1 << ord(letter) - ord('a')

print(dfs(0, learnt))
