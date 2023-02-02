fib = [0, 1]

for i in range(2, 10001):
    fib.append(fib[i - 1] + fib[i - 2])

n = int(input())
print(fib[n])