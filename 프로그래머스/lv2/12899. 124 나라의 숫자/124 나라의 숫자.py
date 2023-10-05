def solution(n):
    result = list()

    while n:
        chk = n % 3
        if chk == 0:
            result.append('4')
            n -= 1
        elif chk == 1: result.append('1')
        else: result.append('2')
        n //= 3

    return ''.join(result[::-1])