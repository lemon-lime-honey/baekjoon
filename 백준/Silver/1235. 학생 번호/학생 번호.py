n = int(input())

cnt = [set() for i in range(100)]

for i in range(n):
    num = input()
    for j in range(len(num)):
        cnt[j].add(num[len(num) - j - 1 :])

for i in range(100):
    if len(cnt[i]) == n:
        print(i + 1)
        break
