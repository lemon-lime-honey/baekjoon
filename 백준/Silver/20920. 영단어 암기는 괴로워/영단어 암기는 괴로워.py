import sys

words = dict()
n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    ipt = sys.stdin.readline().strip()
    if len(ipt) >= m:
        if ipt not in words:
            words[ipt] = 1
        else:
            words[ipt] += 1

result = sorted(words, key=lambda x: (-1 * words[x], -1 * len(x), x))
print(*result, sep='\n')