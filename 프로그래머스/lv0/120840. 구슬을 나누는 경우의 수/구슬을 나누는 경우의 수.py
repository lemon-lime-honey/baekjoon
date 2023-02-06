def solution(balls, share):
    num1 = balls
    num2 = max(share, balls - share)
    num3 = min(share, balls - share)
    answer = 1

    while num1:
        if num1 > num2:
            answer *= num1
            num1 -= 1
        elif num1 > num3:
            num1 -= 1
        else:
            answer //= num1
            num1 -= 1
    
    return answer