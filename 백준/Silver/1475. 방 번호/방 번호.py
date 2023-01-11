number = input()
cnt = [0] * 10

for num in number:
    cnt[int(num)] += 1

temp = int(cnt[6]) + int(cnt[9])
if temp % 2 == 1:
    temp = temp // 2 + 1
else:
    temp = temp // 2
cnt[6] = temp
cnt[9] = temp

print(max(cnt))