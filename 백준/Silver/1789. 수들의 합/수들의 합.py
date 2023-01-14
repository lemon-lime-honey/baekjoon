def sum(num):
    return (num * (num + 1)) // 2
n = int(input())
m = 1
while True:
    ref = sum(m)
    if (ref <= n) * ((n - ref) <= m):
        print(m)
        break
    m += 1