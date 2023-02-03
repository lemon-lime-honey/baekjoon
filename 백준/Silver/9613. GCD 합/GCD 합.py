def get_gcd(n1, n2):
    big = max(n1, n2)
    small = min(n1, n2)
    
    while True:
        if big % small == 0:
            return small
        big, small = small, big % small

t = int(input())

for i in range(t):
    number = list(map(int, input().split()))
    result = 0
    
    for i in range(1, number[0] + 1):
        for j in range(i + 1, number[0] + 1):
            result += get_gcd(number[i], number[j])
    
    print(result)