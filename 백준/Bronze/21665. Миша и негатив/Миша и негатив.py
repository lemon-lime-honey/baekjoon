n, m = map(int, input().split())
original = list()
cnt = 0

for i in range(n):
    original.append(input())

input()

for i in range(n):
    printed = input()
    for index, pixel in enumerate(printed):
        if pixel == original[i][index]:
            cnt += 1

print(cnt)