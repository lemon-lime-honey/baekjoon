def solution(dots):
    x = [dots[i][0] for i in range(4)]
    y = [dots[i][1] for i in range(4)]
    
    answer = (max(x) - min(x)) * (max(y) - min(y))
    return answer