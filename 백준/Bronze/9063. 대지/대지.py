n = int(input())
x = list()
y = list()

for k in range(n):
    i, j = map(int, input().split())
    x.append(i)
    y.append(j)

print((max(x) - min(x)) * (max(y) - min(y)))