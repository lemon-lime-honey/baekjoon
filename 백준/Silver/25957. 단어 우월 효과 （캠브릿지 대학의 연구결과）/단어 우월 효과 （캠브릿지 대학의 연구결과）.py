from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
words = defaultdict(list)

for i in range(n):
    ipt = input().rstrip()
    words[tuple(sorted(list(ipt)))].append(ipt)

m = int(input())
s = input().split()

result = list()

for w in s:
    for word in words[tuple(sorted(list(w)))]:
        if w[0] == word[0] and w[-1] == word[-1]:
            result.append(word)
            break

print(*result)
