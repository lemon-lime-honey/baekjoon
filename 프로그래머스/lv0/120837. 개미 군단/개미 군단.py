def solution(hp):
    answer = 0
    if hp >= 5:
        while hp >= 5:
            answer += 1
            hp -= 5
    if hp >= 3:
        while hp >= 3:
            answer += 1
            hp -= 3
    if hp >= 1:
        while hp >= 1:
            answer += 1
            hp -= 1
    return answer