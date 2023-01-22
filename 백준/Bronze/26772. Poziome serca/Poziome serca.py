heart = [' @@@   @@@ ',
         '@   @ @   @', 
         '@    @    @', 
         '@         @', 
         ' @       @ ', 
         '  @     @  ', 
         '   @   @   ', 
         '    @ @    ', 
         '     @     ']

n = int(input())
for i in range(9):
    for j in range(n):
        print(heart[i], end = ' ')
    print()