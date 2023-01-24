def get_gcd(number):
    while True:
        if number[1] % number[0] == 0:
            return number[0]
        number[0], number[1] = number[1] % number[0], number[0]

num = list(map(int, input().split(':')))
temp = sorted(num)
gcd = get_gcd(temp)
print(f'{num[0] // gcd}:{num[1] // gcd}')