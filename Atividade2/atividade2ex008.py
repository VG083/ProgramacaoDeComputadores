i = 0
while (i >= 0):
    i = int(input('Digite sua idade: '))
    if (i <= 15) and (i >= 0):
        print('Você pertence a 1ª faixa etária de idade')
    elif (i <= 30) and (i >= 16):
        print('Você pertence a 2ª faixa etária de idade')
    elif (i > 30) and (i >= 0):
        print('Você pertence a 3ª faixa etária de idade')