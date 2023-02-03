n = int(input())
stick = 0

while n:
    stick += n % 2
    n //= 2

print(stick)