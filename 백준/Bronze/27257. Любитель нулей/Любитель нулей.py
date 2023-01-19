k = int(input())
kRev = str(int(str(k)[::-1]))
zero = 0

for digit in kRev:
    if digit == '0':
        zero += 1

print(zero)