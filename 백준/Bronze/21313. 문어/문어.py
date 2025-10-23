n = int(input())

result = " ".join("1 2" for i in range(n // 2))

if n % 2:
    result += " 3"

print(result)
