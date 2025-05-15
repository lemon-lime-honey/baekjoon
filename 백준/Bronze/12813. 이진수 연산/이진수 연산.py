a = input()
b = input()

result = list()
temp = list()

for i in range(len(a)):
    if a[i] == b[i] == "1":
        temp.append("1")
    else:
        temp.append("0")

result.append("".join(temp))

temp.clear()

for i in range(len(a)):
    if a[i] == "1" or b[i] == "1":
        temp.append("1")
    else:
        temp.append("0")

result.append("".join(temp))

temp.clear()

for i in range(len(a)):
    if a[i] != b[i]:
        temp.append("1")
    else:
        temp.append("0")

result.append("".join(temp))

temp.clear()

for i in range(len(a)):
    if a[i] == "1":
        temp.append("0")
    else:
        temp.append("1")

result.append("".join(temp))

temp.clear()

for i in range(len(a)):
    if b[i] == "1":
        temp.append("0")
    else:
        temp.append("1")

result.append("".join(temp))

print(*result, sep="\n")
