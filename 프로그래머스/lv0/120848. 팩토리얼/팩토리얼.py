def solution(n):
    answer = 0
    fact = 1
    
    while True:
        if fact > n:
            answer -= 1
            break
        answer += 1
        fact *= answer
    
    return answer