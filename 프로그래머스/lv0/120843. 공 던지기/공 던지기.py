def solution(numbers, k):
    cnt = 1
    answer = 0
    index = 0
    
    while True:
        if index >= len(numbers):
            index -= len(numbers)
        if cnt == k:
            answer = index + 1
            break
        else:
            cnt += 1
            index += 2
    
    return answer