def solution(n):
    one = bin(n).count("1")
    target = n + 1
    
    while True:
        if bin(target).count("1") == one:
            break
        target += 1
            
    return target
        