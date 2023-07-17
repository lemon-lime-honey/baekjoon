def solution(a, b, c):
    if a == b == c:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    if ((a == b) and (b != c)) or ((b == c) and (c != a)) or ((a == c) and (b != c)):
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    return a + b + c