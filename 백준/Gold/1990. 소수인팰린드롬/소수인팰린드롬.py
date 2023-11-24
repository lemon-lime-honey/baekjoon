import sys
input = sys.stdin.readline


def isPalindrome(n, m):
    if n >= m:
        return True
    if chk[n] != chk[m]:
        return False
    return isPalindrome(n + 1, m - 1)


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    
    return True


a, b = map(int, input().split())
palindrome = list()

if b > int(1e7):
    b = int(1e7)

for i in range(a, b + 1):
    chk = str(i)
    if isPalindrome(0, len(chk) - 1):
        palindrome.append(i)

for num in palindrome:
    if isPrime(num):
        sys.stdout.write(f'{num}\n')

print(-1)