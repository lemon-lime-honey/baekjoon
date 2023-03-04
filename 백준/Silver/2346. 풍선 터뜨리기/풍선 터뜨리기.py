from collections import deque

n = int(input())
original = list(map(int, input().split()))
balloon = deque()
result = list()

for i in range(n):
    balloon.append((i + 1, original[i]))

while balloon:
    now = balloon.popleft()
    result.append(now[0])
    if now[1] < 0:
        balloon.rotate(-1 * now[1])
    else:
        balloon.rotate(1 - now[1])

print(*result)