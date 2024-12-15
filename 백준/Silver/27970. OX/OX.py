ipt = input()
result = 0

for i in range(len(ipt)):
    if ipt[i] == "O":
        result += 2**i
        result %= int(1e9) + 7

print(result)
