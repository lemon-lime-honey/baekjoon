from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().rstrip() for i in range(n)]
answer = list()
dist = 0

for i in range(m):
    cnt = defaultdict(int)

    for j in range(n):
        cnt[dna[j][i]] += 1

    letter = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    answer.append(letter[0][0])

    for k in range(1, len(letter)):
        dist += letter[k][1]

print(''.join(answer), dist, sep='\n')