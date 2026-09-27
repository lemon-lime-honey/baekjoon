def solution(people, limit):
    people.sort()
    lo, hi, answer = 0, len(people) - 1, 0
    
    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1
        hi -= 1
        answer += 1
        
    return answer