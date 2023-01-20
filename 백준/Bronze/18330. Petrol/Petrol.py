n = int(input())
k = int(input())
limit = 60 +k
result = 0

if n <= limit:
    result = n * 1500
else:
    result = limit * 1500 + (n - limit) * 3000

print(result)