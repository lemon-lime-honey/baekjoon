def solution(n):
    answer = 0
    num = n

    while num != 0:
        total = num
        target = num - 1
        while total < n and target > 0:
            total += target
            target -= 1
        if total == n:
            answer += 1
        num -= 1
    
    return answer