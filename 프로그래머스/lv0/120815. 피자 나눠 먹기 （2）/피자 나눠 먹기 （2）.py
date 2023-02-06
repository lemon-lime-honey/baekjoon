def solution(n):
    answer = 1
    
    while True:
        if not (answer * 6) % n:
            return answer
        answer += 1