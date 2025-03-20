word = input()
result = [".", ".", "#", ".", "."]

for idx, letter in enumerate(word):
    if (idx + 1) % 3 == 0:
        result[0] += ".*.."
        result[1] += "*.*."
        result[2] = result[2][:-1] + "*." + letter + ".*"
        result[3] += "*.*."
        result[4] += ".*.."
    else:
        result[0] += ".#.."
        result[1] += "#.#."
        result[2] += "." + letter + ".#"
        result[3] += "#.#."
        result[4] += ".#.."

for line in result:
    print(line)
