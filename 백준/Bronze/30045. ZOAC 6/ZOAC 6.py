n = int(input())
result = 0

for i in range(n):
    ipt = input()
    if "01" in ipt or "OI" in ipt:
        result += 1

print(result)