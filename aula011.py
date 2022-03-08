contador = 0
for a in range (0,10,1):
    a = int(input('Digite uma idade: '))
    if a >= 12:
        contador += 1
    if a <= 17:
        contador += 1
print('Há {} pessoas adolescentes entre 12 e 17 anos'.format(contador - 10))
