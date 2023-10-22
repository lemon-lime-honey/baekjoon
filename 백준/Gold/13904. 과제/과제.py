import heapq, sys
input = sys.stdin.readline

n = int(input())
assignment = list()
max_day = 0
result = 0

for i in range(n):
    d, w = map(int, input().split())
    heapq.heappush(assignment, (-w, d))
    max_day = max(max_day, d)

table = [0 for i in range(max_day + 1)]

while assignment:
    score, limit = heapq.heappop(assignment)
    for i in range(max_day, 0, -1):
        if not table[i] and i <= limit:
            table[i] = -score
            break

print(sum(table))