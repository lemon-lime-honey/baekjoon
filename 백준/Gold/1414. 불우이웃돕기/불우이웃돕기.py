import sys
input = sys.stdin.readline


def find(p):
    if p != connection[p]:
        connection[p] = find(connection[p])
    return connection[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q: return True
    if p < q: connection[q] = p
    else: connection[p] = q
    return False


total = 0
result = 0
n = int(input())
cables = list()
connection = [i for i in range(n)]

for i in range(n):
    ipt = input().rstrip()
    for j in range(n):
        if ipt[j] == '0': continue
        length = 0
        if ipt[j] < 'a':
            length = ord(ipt[j]) - ord('A') + 27
        else:
            length = ord(ipt[j]) - ord('a') + 1
        total += length
        cables.append((i, j, length))

cables.sort(key=lambda x:x[2])

for start, end, dist in cables:
    if union(start, end): continue
    result += dist

for i in range(n):
    find(i)
    if connection[i] != 0:
        print(-1)
        break
else:
    print(total - result)