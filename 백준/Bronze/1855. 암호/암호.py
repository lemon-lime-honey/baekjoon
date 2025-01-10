k = int(input())
password = input()

arr = [[] for i in range(k)]
direction = True
idx = 0

for i in range(len(password)):
    arr[idx].append(password[i])
    if direction:
        idx += 1
        if idx == k:
            idx = k - 1
            direction = False
    else:
        idx -= 1
        if idx == -1:
            idx = 0
            direction = True

for line in arr:
    print(*line, sep="", end="")