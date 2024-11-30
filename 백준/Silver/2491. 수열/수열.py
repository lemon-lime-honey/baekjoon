n = int(input())
arr = list(map(int, input().split()))

asc, desc = [1 for i in range(n)], [1 for i in range(n)]

for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        asc[i] = asc[i - 1] + 1
    if arr[i - 1] >= arr[i]:
        desc[i] = desc[i - 1] + 1

print(max(max(asc), max(desc)))
