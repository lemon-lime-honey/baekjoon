def get_gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        gcd = get_gcd(max(answer, arr[i]), min(answer, arr[i]))
        answer = answer * arr[i] // gcd
        
    return answer