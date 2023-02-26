n = int(input())
lst = [0] * (10 ** 6 + 1)

for i in range(2, 10 ** 6 + 1):
    lst[i] = lst[i - 1] + 1
    if not i % 3:
        lst[i] = min(lst[i // 3] + 1, lst[i])
    if not i % 2:
        lst[i] = min(lst[i // 2] + 1, lst[i])

print(lst[n])