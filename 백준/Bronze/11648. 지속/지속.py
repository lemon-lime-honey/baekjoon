result = 0

ipt = input()

while len(ipt) > 1:
    nums = list(map(int, list(ipt)))
    num = 1

    for n in nums:
        num *= n

    ipt = str(num)
    result += 1

print(result)
