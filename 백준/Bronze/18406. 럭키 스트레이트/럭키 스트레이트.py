ipt = input()
left, right = 0, 0

for i in range(len(ipt)):
    if i < len(ipt) // 2:
        left += int(ipt[i])
    else:
        right += int(ipt[i])

print('LUCKY' if left == right else 'READY')