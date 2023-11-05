n, k = map(int, input().split())
countries = list()
target = None

for i in range(n):
    num, g, s, b = map(int, input().split())
    if num == k:
        target = (g, s, b)
    countries.append((num, g, s, b))

countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
result = 0

for i in range(n):
    result += 1
    if countries[i][1:] == target: break

print(result)