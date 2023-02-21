def solution(n):
    three = list()
    answer = 0
    ref = 0
    
    while n:
        three.append(n % 3)
        n //= 3
    
    while three:
        answer += three.pop() * (3 ** ref)
        ref += 1
    
    return answer