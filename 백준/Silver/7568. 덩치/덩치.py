n = int(input())
data = list()

for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)

for i in range(n):
    cnt = 1
    for j in range(n):
        if (i != n) * (data[i][0] < data[j][0]) * (data[i][1] < data[j][1]):
            cnt += 1
    print(cnt, end = ' ')