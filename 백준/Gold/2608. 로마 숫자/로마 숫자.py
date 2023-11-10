r2a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
a2r = {
    1: 'I',
    5: 'V', 4: 'IV',
    10: 'X', 9: 'IX',
    50: 'L', 40: 'XL',
    100: 'C', 90: 'XC',
    500: 'D', 400: 'CD',
    1000: 'M', 900: 'CM'
}


def toRoman(arabic):
    result = list()

    for num in sorted(a2r.keys(), reverse=True):
        while num <= arabic:
            result.append(a2r[num])
            arabic -= num

    return ''.join(result)


def toArabic(roman):
    idx, n = 0, len(roman)
    result = 0

    while idx < n:
        if idx == n - 1:
            result += r2a[roman[idx]]
            break
        if r2a[roman[idx]] < r2a[roman[idx + 1]]:
            result += r2a[roman[idx + 1]] - r2a[roman[idx]]
            idx += 2
        else:
            result += r2a[roman[idx]]
            idx += 1
    
    return result


if __name__ == '__main__':
    one = toArabic(input())
    two = toArabic(input())

    result_arabic = one + two
    result_roman = toRoman(result_arabic)

    print(result_arabic, result_roman, sep='\n')