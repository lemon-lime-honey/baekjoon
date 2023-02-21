def solution(arr, divisor):
    answer = list()
    arr.sort()
    
    for number in arr:
        if not number % divisor:
            answer.append(number)
    
    if not len(answer):
        answer.append(-1)
    
    return answer