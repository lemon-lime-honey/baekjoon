n, b = input().split()
target = n[::-1]
result = 0
b = int(b)

for i in range(len(n)):
    if target[i].isalpha():
        result += (ord(target[i]) - 55) * (b ** i)
    else:
        result += int(target[i]) * (b ** i)

print(result)