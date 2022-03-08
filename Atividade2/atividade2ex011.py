cs = 0
cn = 0
for c in range (0,15,1):
    c = int(input('Você gosta de beterraba? (1 para sim / 2 para não) '))
    if (c == 1):
        cs += 1
    elif (c == 2):
        cn += 1
print(' ')
print('{} pessoas gostam de beterrada'.format(cs))
print('{} pessoas não gostam de beterraba'.format(cn))