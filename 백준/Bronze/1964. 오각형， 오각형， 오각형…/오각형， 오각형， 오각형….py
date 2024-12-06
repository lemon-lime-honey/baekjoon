n = int(input())
result = 5

for i in range(3, n + 2):
    result += i * 3 - 2
    result %= 45678

print(result)