def chk(number):
    for i in range(1, number + 1):
        if (i in range(2, number)) and not (number % i):
            return 1
    return 0

def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        answer += chk(i)
    
    return answer