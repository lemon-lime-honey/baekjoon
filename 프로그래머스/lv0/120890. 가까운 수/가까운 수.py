def solution(array, n):
    dist = 1000
    answer = 1000
    
    for num in array:
        if abs(num - n) < dist:
            answer = num
            dist = abs(num - n)
        elif abs(num - n) == dist:
            if num < answer:
                answer = num
    
    return answer