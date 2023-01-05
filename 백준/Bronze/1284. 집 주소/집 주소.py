import sys

space = {'0': 4, '1': 2, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3}
while True:
    temp = sys.stdin.readline().strip()
    if temp == '0':
        break
    result = 1 + len(temp)
    for num in temp:
        result += space[num]
    print(result)