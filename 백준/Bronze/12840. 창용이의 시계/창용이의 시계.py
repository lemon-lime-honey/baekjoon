h, m, s = map(int, input().split())
time = h * 60 * 60 + m * 60 + s
day = 24 * 60 * 60
q = int(input())

result = list()

for i in range(q):
    ipt = list(map(int, input().split()))

    match ipt[0]:
        case 1:
            time = (time + ipt[1]) % day
        case 2:
            time = (time - ipt[1]) % day
        case 3:
            second = time % 60
            minute = (time % 3600) // 60
            hour = time // 3600
            result.append(f"{hour} {minute} {second}")

print(*result, sep="\n")
