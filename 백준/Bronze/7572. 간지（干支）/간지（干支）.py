n = int(input())
result = list()

first = "ABCDEFGHIJKL"
second = "0123456789"

if n < 1984:
    chk = 1984 - n
    result.append(first[-chk % 12])
    result.append(second[-chk % 10])
else:
    chk = n - 1984
    result.append(first[chk % 12])
    result.append(second[chk % 10])

print("".join(result))
