import datetime

t = int(input())

for i in range(t):
    temp = list(map(int, input().split()))
    start = datetime.date(2023, temp[0], temp[1])
    end = datetime.date(2023, temp[2], temp[3])
    print(f'#{i + 1} {(end - start).days + 1}')