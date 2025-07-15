ipt = input()
result, idx = 0, 0

while idx < len(ipt) - 3:
    if ipt[idx:idx + 4] == "DKSH":
        result += 1
        idx += 4
    else:
        idx += 1

print(result)
