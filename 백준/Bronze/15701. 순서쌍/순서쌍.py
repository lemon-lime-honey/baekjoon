n = int(input())
result = 0

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if i * i == n:
            result += 1
        else:
            result += 2
            

print(result)