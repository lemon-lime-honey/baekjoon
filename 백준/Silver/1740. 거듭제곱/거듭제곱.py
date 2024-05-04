n = bin(int(input()))[2:]
exp = len(n) - 1
result = 0

for num in n:
    if int(num):
        result += 3 ** exp
    exp -= 1

print(result)