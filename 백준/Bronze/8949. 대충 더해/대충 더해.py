a, b = input().split()
i, j = len(a) - 1, len(b) - 1

result = list()

while i >= 0 and j >= 0:
    result.append(str(int(a[i]) + int(b[j])))
    i -= 1
    j -= 1

if i >= 0:
    result.append(a[: i + 1])
if j >= 0:
    result.append(b[: j + 1])

print("".join(result[::-1]))
