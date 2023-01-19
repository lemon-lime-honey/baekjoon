w = int(input())
l = int(input())
h = int(input())

if ((min(w, l) / h) >= 2) * ((max(w, l) / min(w, l)) <= 2):
    print('good')
else:
    print('bad')