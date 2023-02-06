def solution(order):
    answer = 0
    
    while order:
        if order % 10 in (3, 6, 9):
            answer += 1
        order //= 10
    
    return answer