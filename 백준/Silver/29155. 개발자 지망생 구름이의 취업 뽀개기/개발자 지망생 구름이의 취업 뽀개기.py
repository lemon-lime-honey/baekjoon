import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
q = [list(map(int, input().split())) for i in range(n)]
q.sort(key=lambda x: (x[0], x[1]))

cnt = [0 for i in range(6)]
result = q[0][1]
cnt[q[0][0]] = 1
last = 0

for i in range(1, n):
    if cnt[q[i][0]] == p[q[i][0] - 1]: continue
    cnt[q[i][0]] += 1
    if q[last][0] == q[i][0]:
        result += 2 * q[i][1] - q[last][1]
    else:
        result += 60 + q[i][1]
    last = i

print(result)