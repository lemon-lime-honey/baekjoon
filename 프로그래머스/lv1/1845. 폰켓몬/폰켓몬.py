from collections import Counter

def solution(nums):
    numbers = Counter(nums)
    answer = min(len(nums) // 2, len(numbers))
    return answer