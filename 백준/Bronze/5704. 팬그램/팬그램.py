while True:
    ipt = input()

    if ipt == "*":
        break

    chk = set()

    for letter in ipt:
        if letter == " ":
            continue
        chk.add(letter)
 
    if len(chk) == 26:
        print("Y")
    else:
        print("N")
