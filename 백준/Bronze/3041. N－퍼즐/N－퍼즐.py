coord = list()
result = 0

for i in range(4):
    for j in range(4):
        coord.append((i, j))

for i in range(4):
    ipt = input()
    for j in range(4):
        if ipt[j] == ".":
            continue
        target = coord[ord(ipt[j]) - ord("A")]
        result += abs(i - target[0]) + abs(j - target[1])

print(result)
