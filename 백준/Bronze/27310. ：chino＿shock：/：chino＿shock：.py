emoji = input()
difficulty = len(emoji)

for element in emoji:
    if element == ':':
        difficulty += 1
    elif element == '_':
        difficulty += 5

print(difficulty)