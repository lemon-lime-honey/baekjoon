strokes = [3, 2, 1,	2, 3, 3, 3,	3, 1, 1, 3, 1, 3,
           3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

string = input()
score = 0

for letter in string:
    score += strokes[ord(letter) - ord('A')]

print("I'm a winner!" if score % 2 else "You're the winner?")