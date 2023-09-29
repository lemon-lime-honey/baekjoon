import sys
input = sys.stdin.readline

n, m = map(int, input().split())
row, col = set(), set()

for i in range(n):
    ipt = input().rstrip()
    for j in range(m):
        if ipt[j] == 'X':
            row.add(i)
            col.add(j)

print(max(n - len(row), m - len(col)))