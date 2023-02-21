def get_gcd(n1, n2):
    while True:
        if not (n1 % n2):
            return n2
        n1, n2 = n2, n1 % n2

def solution(n, m):
    answer = list()
    gcd = get_gcd(max(n, m), min(n, m))
    answer.append(gcd)
    answer.append(m * n // gcd)

    return answer