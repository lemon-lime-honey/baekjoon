import heapq, sys
input = sys.stdin.readline


def find(p):
    if p != planet[p]:
        planet[p] = find(planet[p])
    return planet[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2: return True
    if p1 <= p2: planet[p2] = p1
    else: planet[p1] = p2
    return False


n = int(input())
coord = list()

for i in range(n):
    data = list(map(int, input().split()))
    coord.append(data + [i])

x = sorted(coord, key=lambda x:x[0])
y = sorted(coord, key=lambda x:x[1])
z = sorted(coord, key=lambda x:x[2])

planet = [i for i in range(n)]
paths = list()
result = 0
ref = 0

for i in range(n - 1):
    heapq.heappush(paths, (abs(x[i][0] - x[i + 1][0]), x[i][3], x[i + 1][3]))
    heapq.heappush(paths, (abs(y[i][1] - y[i + 1][1]), y[i][3], y[i + 1][3]))
    heapq.heappush(paths, (abs(z[i][2] - z[i + 1][2]), z[i][3], z[i + 1][3]))

while ref < n - 1:
    cost, start, end = heapq.heappop(paths)
    chk = union(start, end)
    if not chk:
        result += cost
        ref += 1

print(result)