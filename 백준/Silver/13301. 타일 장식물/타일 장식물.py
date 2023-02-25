fib = [1, 1]
for i in range(80):
    fib.append(fib[-1] + fib[-2])

n = int(input())

if n == 1:
    print(4)
else:
    print(fib[n - 1] * 4 + fib[n - 2] * 2)