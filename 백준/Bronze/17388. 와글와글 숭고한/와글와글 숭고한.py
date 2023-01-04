s, k, h = map(int, input().split())
if (s + k + h) >= 100:
    print('OK')
else:
    temp = min(s, k, h)
    if temp == s:
        print('Soongsil')
    elif temp == k:
        print('Korea')
    elif temp == h:
        print('Hanyang')