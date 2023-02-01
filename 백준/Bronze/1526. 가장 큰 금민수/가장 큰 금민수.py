def chk_num(number):
    while number:
        if (number % 10) not in (4, 7):
            return False
        number //= 10
    return True

n = int(input())
numList = list()

for i in range(n + 1):
    if chk_num(i):
        numList.append(i)

print(numList[-1])