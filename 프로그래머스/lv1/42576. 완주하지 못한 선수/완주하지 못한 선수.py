from collections import Counter

def solution(participant, completion):
    whole = Counter(participant)
    finished = Counter(completion)
    
    answer = list(whole - finished)[0]
    
    return answer