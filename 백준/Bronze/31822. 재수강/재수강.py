target = input()
result = 0

n = int(input())

for i in range(n):
    ipt = input()
    if target[:5] == ipt[:5]:
        result += 1

print(result)
