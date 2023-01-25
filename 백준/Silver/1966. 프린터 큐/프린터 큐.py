from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    docs = deque()

    for index, priority in enumerate(temp):
        docs.append((priority, index))

    cnt = 0
    
    while docs:
        ref = max(docs)
        front = docs.popleft()
        if (ref[0] == front[0]) * (front[1] == m):
            cnt += 1
            print(cnt)
            break
        if (front[0] != ref[0]):
            docs.append(front)
        else:
            cnt += 1
