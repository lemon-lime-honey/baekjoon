import sys

input = sys.stdin.readline

t = int(input())
result = list()

for i in range(t):
    n = int(input())
    fib = [1, 1, 2, 4]

    for j in range(4, n + 1):
        fib.append(fib[-4] + fib[-3] + fib[-2] + fib[-1])

    result.append(fib[n])

print(*result, sep="\n")
