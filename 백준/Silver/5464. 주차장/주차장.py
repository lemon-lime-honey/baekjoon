from collections import deque

n, m = map(int, input().split())

space = [0 for i in range(n + 1)]
car_weights = [0]
que = deque()
cost = [0]
result = 0

for i in range(n):
    cost.append(int(input()))

for i in range(m):
    car_weights.append(int(input()))

for i in range(2 * m):
    ipt = int(input())
    if ipt < 0:
        for j in range(1, n + 1):
            if space[j] == -ipt:
                result += cost[j] * car_weights[-ipt]
                space[j] = 0
                break
        if que:
            while que:
                for j in range(1, n + 1):
                    if space[j] == 0:
                        space[j] = que.popleft()
                        break
                else:
                    break
    else:
        for j in range(1, n + 1):
            if space[j] == 0:
                space[j] = ipt
                break
        else:
            que.append(ipt)

print(result)
