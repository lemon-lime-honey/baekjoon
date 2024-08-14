n = int(input())
stst = input()
result = 0

for i in range(n // 2):
    if stst[i] != stst[n - i - 1]:
        result += 1

print(result)
