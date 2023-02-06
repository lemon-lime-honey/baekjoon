def solution(array):
    answer = [0, 0]
    
    for index, number in enumerate(array):
        if number > answer[0]:
            answer[0] = number
            answer[1] = index
    
    return answer