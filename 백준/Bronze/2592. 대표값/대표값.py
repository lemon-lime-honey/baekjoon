number = list()
num_count = dict()

for i in range(10):
    number.append(int(input()))
    if number[i] in num_count:
        num_count[number[i]] += 1
    else:
        num_count[number[i]] = 1

num_count = sorted(num_count.items(), key = lambda x: x[1], reverse = True)

print(f'{sum(number) // 10}\n{num_count[0][0]}')