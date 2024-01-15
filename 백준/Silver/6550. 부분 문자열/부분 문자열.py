def chk():
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            j += 1
        else:
            i += 1
            j += 1

    if i == len(s):
        return True
    return False


while True:
    try:
        s, t = input().split()
        print('Yes' if chk() else 'No')
    except:
        break