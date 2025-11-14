n = int(input())

result = "%.300f" % 2**-n
idx = len(result)

for i in range(idx - 1, 1, -1):
    if result[i] != "0":
        end = i
        break

print(result[: end + 1])
