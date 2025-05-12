binary = input()
result = 0
idx = 0

for i in range(len(binary) - 1, -1, -1):
    result += int(binary[i]) * 2 ** idx
    idx += 1

print(oct(result)[2:])
