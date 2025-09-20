q = int(input())

for i in range(q):
    a, m = map(int, input().split())
    print(int(a * m * 105.6 / 1000 / 60))
