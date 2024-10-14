import sys

input = sys.stdin.readline

n, g = input().split()
result, cnt = 0, 0
seen = set()

for i in range(int(n)):
    name = input().rstrip()

    if name in seen:
        continue

    seen.add(name)
    cnt += 1

    match g:
        case "Y":
            if cnt == 1:
                result += 1
                cnt = 0
        case "F":
            if cnt == 2:
                result += 1
                cnt = 0
        case "O":
            if cnt == 3:
                result += 1
                cnt = 0

print(result)
