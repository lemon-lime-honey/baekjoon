def solution(n):
    answer = list()
    
    for i in range(n):
        if i % 2:
            answer.append('박')
        else:
            answer.append('수')
    
    return (''.join(answer))