address = input().split(":")
result = list()
flag = False

for part in address:
    if not part and not flag:
        for i in range(8 - len(address) + 1):
            result.append("0000")
        flag = True
    else:
        result.append(part.rjust(4, "0"))

print(':'.join(result))