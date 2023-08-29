from collections import defaultdict

n, x = map(int, input().split())
visited = list(map(int, input().split()))
lo, hi = 0, x - 1
cnt = defaultdict(int)
max_num = 0
temp = 0

for i in range(lo, hi + 1):
    temp += visited[i]

cnt[temp] += 1
lo += 1
hi += 1

while hi < n:
    temp -= visited[lo - 1]
    temp += visited[hi]
    cnt[temp] += 1
    lo += 1
    hi += 1

result = sorted(cnt.items(), key=lambda x:x[0], reverse=True)

if result[0][0] != 0:
    print(result[0][0], result[0][1], sep='\n')
else: print("SAD")