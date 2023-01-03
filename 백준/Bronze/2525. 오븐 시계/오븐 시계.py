time = list(map(int, input().split()))
cook = int(input())
time[1] += cook
if time[1] > 59:
    hour = time[1] // 60
    time[0] += hour
    time[1] = time[1] % 60
if time[0] > 23:
    time[0] = time[0] % 24
print(' '.join(map(str, time)))