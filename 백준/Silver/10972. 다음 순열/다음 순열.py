n = int(input())
target = list(map(int, input().split()))
flag = False

i = n - 1

while i > 0 and target[i - 1] >= target[i]:
    i -= 1

if i <= 0: flag = True

if not flag:
    j = n - 1

    while target[i - 1] >= target[j]:
        j -= 1

    target[i - 1], target[j] = target[j], target[i - 1]

    j = n - 1

    while i < j:
        target[i], target[j] = target[j], target[i]
        i += 1
        j -= 1

if flag:
    print(-1)
else:
    print(*target)