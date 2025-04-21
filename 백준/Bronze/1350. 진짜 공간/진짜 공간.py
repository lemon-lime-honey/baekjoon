n = int(input())
files = list(map(int, input().split()))
cluster = int(input())
result = 0

for file in files:
    if file % cluster:
        result += file // cluster + 1
    else:
        result += file // cluster

result *= cluster

print(result)
