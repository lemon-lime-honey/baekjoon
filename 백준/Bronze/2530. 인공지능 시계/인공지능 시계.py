hour, min, sec = map(int, input().split())
time = int(input())
sec += time
temp = sec // 60
sec %= 60
min += temp
temp = min // 60
min %= 60
hour += temp
hour %= 24
print(f'{hour} {min} {sec}')