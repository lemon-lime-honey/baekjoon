sieve = [False, False] + [True] * 9999

for i in range(2, 101):
    if sieve[i]:
        for j in range(2 * i, 10001, i):
            sieve[j] = False

def solution(n):
    answer = list()
    
    for i in range(1, n + 1):
        if not (n % i) and sieve[i]:
            answer.append(i)
    
    return answer