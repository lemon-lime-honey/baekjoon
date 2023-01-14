result = [0] * 10001

for i in range(1, 10001):
    total = i
    num = i
    while i > 0:
        total += i % 10
        i = i // 10
    if total <= 10000:
        result[total] += 1

for index, value in enumerate(result):
    if index == 0:
        continue
    if value == 0:
        print(index)