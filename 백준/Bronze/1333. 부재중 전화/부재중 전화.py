n, l, d = map(int, input().split())
time = l * n + 5 * (n - 1)
frame = [False for i in range(time + 1)]

for i in range(0, time, l + 5):
    for j in range(i, i + l):
        frame[j] = True

for i in range(0, time, d):
    if not frame[i]:
        print(i)
        break
else:
    print(i + d)
