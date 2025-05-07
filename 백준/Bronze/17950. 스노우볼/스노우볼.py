h, x = map(int, input().split())
result = 0
num = 1

for i in range(h):
    num = (num * x) % (int(1e9) + 7)
    result = (result + int(input()) * num) % (int(1e9) + 7)

print(result)
