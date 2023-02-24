from collections import deque

n = int(input())
order = list(map(int, input().split()))
result = deque()

for i in range(1, n + 1):
    now = order.pop()
    if now == 1:
        result.appendleft(i)
    elif now == 2:
        temp = result.popleft()
        result.appendleft(i)
        result.appendleft(temp)
    elif now == 3:
        result.append(i)

print(*result)