def solution(t, p):
    len_t = len(t)
    len_p = len(p)
    answer = 0
    ref = 0
    
    while ref <= (len_t - len_p):
        if int(t[ref: ref + len_p]) <= int(p):
            answer += 1
        ref += 1
    
    return answer