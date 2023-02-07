from collections import deque

def solution(A, B):
    original = deque(A)
    target = deque(B)
    rev = 0

    while rev < len(A):
        if original == target:
            return rev
        rev += 1
        original.rotate(1)
        
    return (-1)