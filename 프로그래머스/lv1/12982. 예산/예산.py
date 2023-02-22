def solution(d, budget):
    d.sort()
    total = 0
    answer = 0
    
    for cost in d:
        total += cost
        if total > budget:
            break
        answer += 1
    
    return answer