real = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

while True:
    ipt = input().split()

    if ipt == ["***"]:
        break

    target = int(input())
    result = list()

    for note in ipt:
        if note not in real:
            if note[-1] == "#":
                temp = real.index(note[0])
                note = real[temp + 1]
            else:
                temp = real.index(note[0])
                if temp == 0:
                    note = "G#"
                else:
                    note = real[temp - 1]

        original = real.index(note)
        idx = original + target

        if idx > 11:
            idx %= 12

        result.append(real[idx])

    print(*result)
