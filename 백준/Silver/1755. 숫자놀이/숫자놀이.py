number = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

m, n = map(int, input().split())

result = list()

for i in range(m, n + 1):
    temp = list()
    target = str(i)
    if len(target) == 1:
        temp.append(number[target])
    else:
        temp.append(number[target[0]])
        temp.append(number[target[1]])
    result.append((" ".join(temp), i))

result.sort()

for i in range(0, len(result), 10):
    print(*[num[1] for num in result[i : i + 10]])
