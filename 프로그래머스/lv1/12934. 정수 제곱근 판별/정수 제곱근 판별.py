from math import sqrt

def solution(n):
    result = int(sqrt(n))
    if n == result ** 2:
        return (result + 1) ** 2
    else:
        return -1