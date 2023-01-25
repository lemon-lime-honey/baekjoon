from collections import deque

n, m = map(int, input().split())
number = deque([x for x in range(1, n + 1)])
target = deque(map(int, input().split()))
cnt = 0

while target:
    if target[0] == number[0]:
        number.popleft()
        target.popleft()
    elif number.index(target[0]) <= len(number) // 2:
        while True:
            number.rotate(-1)
            cnt += 1
            if target[0] == number[0]:
                break
    elif number.index(target[0]) > len(number) // 2:
        while True:
            number.rotate(1)
            cnt += 1
            if target[0] == number[0]:
                break

print(cnt)