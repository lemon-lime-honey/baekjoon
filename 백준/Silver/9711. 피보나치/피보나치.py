import sys

fib = [0, 1]

for i in range(2, 10001):
    fib.append(fib[i - 1] + fib[i - 2])

t = int(sys.stdin.readline())

for i in range(t):
    p, q = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'Case #{i + 1}: {fib[p] % q}\n')