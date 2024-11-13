n = int(input())
channel =list()
idx = [0, 0]

for i in range(n):
    channel.append(input())
    if channel[-1] == "KBS1":
        idx[0] = i
    elif channel[-1] == "KBS2":
        idx[1] = i

result = list()

for i in range(idx[0]):
    result.append(1)

for i in range(idx[0]):
    result.append(4)

if idx[0] > idx[1]:
    idx[1] += 1

for i in range(idx[1]):
    result.append(1)

for i in range(idx[1] - 1):
    result.append(4)

print(*result, sep="")