n = int(input())
lst = input()

idx = 0
result = 0

while idx < n - 3:
    if lst[idx : idx + 4] == "pPAp":
        result += 1
        idx += 4
    else:
        idx += 1

print(result)
