def solution(n):
    result = 0
    for i in range(1, n + 1):
        if not (n % i):
            result += i
    return result