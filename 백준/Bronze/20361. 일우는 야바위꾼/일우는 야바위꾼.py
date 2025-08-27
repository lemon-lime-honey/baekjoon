n, x, k = map(int, input().split())

cup = [0 for i in range(n + 1)]
cup[x] = 1

for i in range(k):
    a, b = map(int, input().split())
    cup[a], cup[b] = cup[b], cup[a]

for i in range(1, n + 1):
    if cup[i] == 1:
        print(i)
        break
