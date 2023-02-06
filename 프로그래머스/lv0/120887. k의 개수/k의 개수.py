def solution(i, j, k):
    answer = 0
    
    for num in range(i, j + 1):
        while num:
            if num % 10 == k:
                answer += 1
            num //= 10
    
    return answer