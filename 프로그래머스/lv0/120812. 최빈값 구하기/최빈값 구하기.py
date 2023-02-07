from collections import Counter

def solution(array):
    numbers = Counter(array)
    answer = numbers.most_common()
    
    if (len(answer) > 1) and (answer[0][1] == answer[1][1]):
        return -1
    
    return answer[0][0]