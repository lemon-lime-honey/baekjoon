def main():
    s = input()
    idx = len(s) - 1

    if s[idx] in "aeiou" or s[idx] in "ns":
        flag = False
    else:
        flag = True

    while idx >= 0:
        if s[idx] in "aeiou":
            if flag:
                return idx + 1
            else:
                flag = True
        idx -= 1

    return -1


if __name__ == "__main__":
    print(main())
