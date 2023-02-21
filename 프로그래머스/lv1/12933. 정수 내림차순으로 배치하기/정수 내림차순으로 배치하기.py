def solution(n):
    answer = list()
    while n:
        answer.append(str(n % 10))
        n //= 10
    answer.sort(reverse = True)
    result = int(''.join(map(str, answer)))
    return result