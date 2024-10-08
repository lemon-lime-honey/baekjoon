import sys

input = sys.stdin.readline

n, m = map(int, input().split())
limit = list(map(int, input().split()))
first = [list(map(int, input().split())) for i in range(n)]
second = [list(map(int, input().split())) for i in range(n)]

result = [[] for i in range(n)]
cnt = [0 for i in range(m)]

for i in range(n):
    for subject in first[i][:-1]:
        cnt[subject - 1] += 1

for i in range(n):
    for subject in first[i][:-1]:
        if cnt[subject - 1] <= limit[subject - 1]:
            result[i].append(subject)

for i in range(n):
    for subject in second[i][:-1]:
        cnt[subject - 1] += 1

for i in range(n):
    for subject in second[i][:-1]:
        if cnt[subject - 1] <= limit[subject - 1]:
            result[i].append(subject)

for i in range(n):
    result[i].sort()

for res in result:
    if not res:
        print("망했어요")
    else:
        print(*res)