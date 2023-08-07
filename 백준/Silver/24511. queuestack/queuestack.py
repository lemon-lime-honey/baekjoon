from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
result = list()

que = deque()

for i in range(n):
    if not a[i]:
        que.append(b[i])

que.extendleft(c)
print(*list(que)[::-1][:m])