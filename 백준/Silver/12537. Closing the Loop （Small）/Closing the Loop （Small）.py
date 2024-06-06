import heapq, sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = int(input())
    ropes = list(input().split())

    r, b = list(), list()

    for rope in ropes:
        if rope[-1] == 'R':
            heapq.heappush(r, -int(rope[:len(rope) - 1]))
        else:
            heapq.heappush(b, -int(rope[:len(rope) - 1]))

    result = 0

    while r and b:
        result -= heapq.heappop(r)
        result -= heapq.heappop(b)
        result -= 2

    print(f'Case #{i + 1}: {result}')