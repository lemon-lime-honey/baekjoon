def solution(clothes):
    wear = dict()
    
    for name, kind in clothes:
        if kind not in wear:
            wear[kind] = 1
        else:
            wear[kind] += 1
    
    quantity = list(wear.values())
    answer = 1

    for element in quantity:
        answer *= element + 1
    
    answer -= 1
    return answer