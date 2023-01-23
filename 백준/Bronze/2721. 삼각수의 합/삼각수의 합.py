def w_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i * sum(range(1, i + 2))
    return total

t = int(input())

for i in range(t):
    n = int(input())
    print(w_n(n))