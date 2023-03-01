numbers = dict()
n, c = map(int, input().split())
original = list(map(int, input().split()))
result = list()

for number in original:
    if number not in numbers:
        numbers[number] = 1
    else:
        numbers[number] += 1

sorted_num = sorted(numbers, key=lambda x: (-1 * numbers[x]))
for number in sorted_num:
    for i in range(numbers[number]):
        result.append(number)

print(*result)