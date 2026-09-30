def solution(wallet, bill):
    long, short = max(wallet), min(wallet)
    l, s = max(bill), min(bill)
    answer = 0
    
    while l > long or short < s:
        answer += 1
        l //= 2
        if l < s:
            l, s = s, l
            
    return answer