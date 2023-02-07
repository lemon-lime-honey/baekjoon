def get_gcd(n1, n2):
    while True:
        if not (n1 % n2):
            return n2
        n1, n2 = n2, n1 % n2

def solution(a, b):
    gcd = get_gcd(max(a, b), min(a, b))
    b //= gcd

    while b > 1:
        if not (b % 2):
            b //= 2
        elif not (b % 5):
            b //= 5
        else:
            return 2
    
    return 1