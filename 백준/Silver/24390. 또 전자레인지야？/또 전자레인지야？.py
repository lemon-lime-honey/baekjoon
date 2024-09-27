time = list(map(int, input().split(":")))
flag = False
result = 0

if time[0] >= 10:
    result += time[0] // 10
    time[0] %= 10

if time[0] >= 1:
    result += time[0]

if time[1] >= 30:
    result += time[1] // 30
    time[1] %= 30
    flag = True

if time[1] >= 10:
    result += time[1] // 10

print(result if flag else result + 1)