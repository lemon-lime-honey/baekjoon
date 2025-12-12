fib = [1, 2]

while True:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] >= 25000:
        break

t = int(input())

for i in range(t):
    x = int(input())
    target = list()
    flag = False

    for j in range(len(fib) - 1, -1, -1):
        if fib[j] <= x:
            flag = True
            target.append(1)
            x -= fib[j]
        elif flag:
            target.append(0)

    target.pop()
    result = 0

    for idx, val in enumerate(target):
        result += fib[len(target) - idx - 1] * val

    print(result)
