def two(n):
    result = 0
    while n:
        n //= 2
        result += n
    return result

def five(n):
    result = 0
    while n:
        n //= 5
        result += n
    return result

n, m = map(int, input().split())
two_n = two(n)
two_m = two(m)
two_nm = two(n - m)
five_n = five(n)
five_m = five(m)
five_nm = five(n - m)

print(min(two_n - (two_m + two_nm), five_n - (five_m + five_nm)))
