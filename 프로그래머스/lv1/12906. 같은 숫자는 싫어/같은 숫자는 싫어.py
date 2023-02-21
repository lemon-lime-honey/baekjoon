def solution(arr):
    answer = list()
    
    for element in arr:
        if not answer:
            answer.append(element)
        elif element != answer[-1]:
            answer.append(element)
    
    return answer