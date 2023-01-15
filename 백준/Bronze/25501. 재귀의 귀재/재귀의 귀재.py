def recursion(s, l, r, cnt):
    cnt[0] += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1, cnt)

def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)

t = int(input())
for i in range(t):
    cnt = [0]
    s = input()
    print(f'{isPalindrome(s, cnt)} {cnt[0]}')