n, m = map(int, input().split())
result = 0

for i in range(n):
    ipt = input()
    if m // 2 < ipt.count("O"):
        result += 1

print(result)
