def get_gcd(n1, n2):
    while True:
        if not n1 % n2:
            return n2
        n1, n2 = n2, n1 % n2


number1 = list(map(int, input().split()))
number2 = list(map(int, input().split()))
gcd1 = get_gcd(max(number1[1], number2[1]), min(number1[1], number2[1]))
result = [(number1[0] * number2[1] + number2[0] * number1[1]) // gcd1, (number1[1] * number2[1] // gcd1)]
gcd2 = get_gcd(max(result), min(result))
print(result[0] // gcd2, result[1] // gcd2)