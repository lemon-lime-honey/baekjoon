from collections import Counter

def solution(k, tangerine):
    nums = Counter(tangerine).most_common()
    answer = 0
    
    for num in nums:
        if k <= 0:
            break
        answer += 1
        k -= num[1]
    
    return answer