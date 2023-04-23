n = int(input())
array = list(map(int, input().split()))
array_rev = array[::-1]
asc = [1 for i in range(n)]
desc = [1 for i in range(n)]
result = 0

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            asc[i] = max(asc[i], asc[j] + 1)
        if array_rev[i] > array_rev[j]:
            desc[i] = max(desc[i], desc[j] + 1)

for i in range(n):
    result = max(result, asc[i] + desc[n - 1 - i] - 1)

print(result)