import sys

fibonacci = [0, 1]
for i in range(2, 46):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    result = list()
    temp = n

    for j in range(45, 0, -1):
        if fibonacci[j] <= temp:
            result.append(fibonacci[j])
            temp -= fibonacci[j]

    print(*result[::-1])