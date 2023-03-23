import sys, heapq
input = sys.stdin.readline

n = int(input())
relationship = [[int(1e9) for i in range(n)] for j in range(n)]

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    relationship[a - 1][b - 1] = relationship[b - 1][a - 1] = 1

for i in range(n):
    relationship[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            relationship[j][k] = min(relationship[j][k], relationship[j][i] + relationship[i][k])

result = list()

for i in range(n):
    chk = 0
    for j in range(n):
        chk = max(chk, relationship[i][j])
    heapq.heappush(result, (chk, i + 1))

first_line = [0, 0]
second_line = list()

while result:
    score, person = heapq.heappop(result)
    if not second_line:
        first_line[0] = score
        first_line[1] += 1
        second_line.append(person)
    else:
        if score == first_line[0]:
            first_line[1] += 1
            second_line.append(person)
        else:
            break

print(*first_line)
print(*second_line)
