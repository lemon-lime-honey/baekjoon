board = {'=': '-', '-': '0', '0': '9', '9': '8', '8': '7', 
         '7': '6', '6': '5', '5': '4', '4': '3', '3': '2', 
         '2': '1', '1': '`', '\\': ']', ']': '[', '[': 'P', 
         'P': 'O', 'O': 'I', 'I': 'U', 'U': 'Y', 'Y': 'T', 
         'T': 'R', 'R': 'E', 'E': 'W', 'W': 'Q', '\n': '\'', 
         '\'': ';', ';': 'L', 'L': 'K', 'K': 'J', 'J': 'H', 
         'H': 'G', 'G': 'F', 'F': 'D', 'D': 'S', 'S': 'A', 
         '/': '.', '.': ',', ',': 'M', 'M': 'N', 'N': 'B', 
         'B': 'V', 'V': 'C', 'C': 'X', 'X': 'Z', ' ': ' '}

while True:
    try:
        sentence = input()
        for letter in sentence:
            print(board[letter], end = '')
        print()
    except:
        break