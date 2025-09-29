n, b = map(int, input().split())

cnt = 1

for i in range(1, b + 1):
    cnt += 2**i

if n <= cnt:
    print("yes")
else:
    print("no")
