def solution(array):
    answer = 0
    
    for num in array:
        while num:
            if num % 10 == 7:
                answer += 1
            num //= 10
    
    return answer