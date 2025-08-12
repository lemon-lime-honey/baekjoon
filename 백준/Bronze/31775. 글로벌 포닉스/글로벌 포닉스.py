letters = {"l", "k", "p"}

letters.discard(input()[0])
letters.discard(input()[0])
letters.discard(input()[0])

print("GLOBAL" if len(letters) == 0 else "PONIX")
