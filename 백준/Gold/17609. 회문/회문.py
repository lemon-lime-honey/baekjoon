n = int(input())

def palindrome(string, lo, hi, delete):
    while lo < hi:
        if string[lo] == string[hi]:
            lo += 1
            hi -= 1
        else:
            if delete: return 2
            one = palindrome(string, lo + 1, hi, True)
            two = palindrome(string, lo, hi - 1, True)
            if not one or not two: return 1
            else: return 2
    return 0

for i in range(n):
    target = list(input())
    result = palindrome(target, 0, len(target) - 1, False)
    print(result)