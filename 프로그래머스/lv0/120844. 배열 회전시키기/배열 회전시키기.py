from collections import deque

def solution(numbers, direction):
    if direction == 'right':
        dir = 1
    else:
        dir = -1
    
    numbers = deque(numbers)
    numbers.rotate(dir)
    answer = list(numbers)
    
    return answer