#1 regular
#2 bom
#3 ótimo
cr = 0
cb = 0
co = 0
for c in range (0,15,1):
    c = int(input('O que você achou do filme? (1. Regular / 2. Bom / 3. Ótimo) '))
    if (c == 1):
        cr += 1
    elif (c == 2):
        cb += 1
    elif (c == 3):
        co += 1
print(' ')
print('{} pessoas acharam o filme regular'.format(cr))
print('{} pessoas acharam o filme bom'.format(cb))
print('{} pessoas acharam o filme ótimo'.format(co))
