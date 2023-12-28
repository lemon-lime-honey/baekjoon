import heapq, sys
input = sys.stdin.readline

n = int(input())
result = list()

for i in range(n):
    heapq.heappush(result, int(input()))

while result:
    sys.stdout.write(f'{heapq.heappop(result)}')
    sys.stdout.write('\n')