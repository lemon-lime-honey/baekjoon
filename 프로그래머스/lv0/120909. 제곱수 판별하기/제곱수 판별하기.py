def solution(n):
    factor = list()
    for i in range(1, n + 1):
        if not (n % i):
            factor.append(i)
    if len(factor) % 2:
        answer = 1
    else:
        answer = 2
    return answer