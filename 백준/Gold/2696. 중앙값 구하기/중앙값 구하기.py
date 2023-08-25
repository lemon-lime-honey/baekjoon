from math import ceil
import heapq, sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    m = int(input())
    raw = list()

    for j in range(ceil(m / 10)):
        raw.extend(list(map(int, input().split())))

    result = list()
    small = list()
    temp = list()
    big = list()
    cnt = 0

    for index, num in enumerate(raw):
        if len(small) == len(big):
            heapq.heappush(small, (-num, num))
        else:
            heapq.heappush(big, (num, num))

        if big and small[0][1] > big[0][1]:
            t1 = heapq.heappop(small)[1]
            t2 = heapq.heappop(big)[1]
            heapq.heappush(big, (t1, t1))
            heapq.heappush(small, (-t2, t2))

        if not index % 2:
            cnt += 1
            if len(temp) < 10:
                temp.append(small[0][1])
            else:
                result.append(temp)
                temp = [small[0][1]]

    if temp: result.append(temp)

    print(cnt)

    for nums in result:
        print(*nums)