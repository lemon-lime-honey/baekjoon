def solution(before, after):
    beforeList = sorted(list(before))
    afterList = sorted(list(after))
    
    if beforeList == afterList:
        answer = 1
    else:
        answer = 0
    
    return answer