def get_gcd(number):
    while True:
        if number[1] % number[0] == 0:
            return number[0]
        number[0], number[1] = number[1] % number[0], number[0]

num = list(map(int, input().split()))
temp = sorted(num)
print(num[0] * num[1] // get_gcd(temp))