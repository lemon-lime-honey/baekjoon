n = int(input())
numbers = sorted(list(map(int, input().split())))

result = 0

for i in range(n):
    lo, hi = 0, n - 1

    while lo < hi:
        chk = numbers[lo] + numbers[hi]
        if chk == numbers[i]:
            if lo == i: lo += 1
            elif hi == i: hi -= 1
            else:
                result += 1
                break
        elif chk < numbers[i]: lo += 1
        else: hi -= 1

print(result)