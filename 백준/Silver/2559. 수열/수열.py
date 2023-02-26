n, k = map(int, input().split())
temperature = list(map(int, input().split()))
result = -10 ** 6
calc = 0
start = 0
end = k

while end <= n:
    if start > 0:
        calc = calc - temperature[start - 1] + temperature[end - 1]
    else:
        calc = sum(temperature[start:end])
    if calc > result:
        result = calc
    start += 1
    end += 1

print(result)