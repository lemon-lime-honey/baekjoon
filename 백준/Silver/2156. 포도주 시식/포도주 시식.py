import sys

n = int(sys.stdin.readline())
result = [0] * n
wine = list()

for i in range(n):
    wine.append(int(sys.stdin.readline()))

if n < 3:
    print(sum(wine))
else:
    result[0] = wine[0]
    result[1] = wine[0] + wine[1]
    result[2] = max(wine[0] + wine[2], wine[1] + wine[2], result[1])

    for i in range(3, n):
        result[i] = max(result[i - 3] + wine[i - 1] + wine[i], result[i - 2] + wine[i], result[i - 1])

    print(max(result))