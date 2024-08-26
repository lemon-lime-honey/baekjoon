ipt = input()
result = 1

for i in range(len(ipt)):
    if i == 0:
        if ipt[i] == 'c':
            result *= 26
            result %= 1000000009
        else:
            result *= 10
            result %= 1000000009
    else:
        if ipt[i] == 'c':
            if ipt[i - 1] == 'c':
                result *= 25
                result %= 1000000009
            else:
                result *= 26
                result %= 1000000009
        else:
            if ipt[i - 1] == 'c':
                result *= 10
                result %= 1000000009
            else:
                result *= 9
                result %= 1000000009

print(result)
