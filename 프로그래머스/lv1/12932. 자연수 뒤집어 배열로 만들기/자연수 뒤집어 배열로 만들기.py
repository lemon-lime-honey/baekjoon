def solution(n):
    answer = list()
    while n:
        answer.append(n % 10)
        n //= 10
    return answer