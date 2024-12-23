n = int(input())
arr = list(map(int, input().split()))
flag = False

i = n - 1

while n > 0 and arr[i - 1] < arr[i]:
    i -= 1

if i <= 0:
    flag = True

if not flag:
    j = n - 1
    while arr[i - 1] < arr[j]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    j = n - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

if flag:
    print(-1)
else:
    print(*arr)
