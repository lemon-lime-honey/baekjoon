a, b, c = map(int, input().split())

result = 0
cnt = [0 for i in range(101)]

for i in range(3):
    s, e = map(int, input().split())
    for j in range(s, e):
        cnt[j] += 1

for i in range(1, 101):
    match cnt[i]:
        case 1:
            result += a
        case 2:
            result += 2 * b
        case 3:
            result += 3 * c

print(result)
