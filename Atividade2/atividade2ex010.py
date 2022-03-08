c = 1
while (c != 0):
    c = int(input('Digite o código do produto: '))
    if (c == 1):
        print('Caderno - R$ 12.00')
    elif (c == 2):
        print('Régua - R$ 2.50')
    elif (c == 3):
        print('Borracha - R$ 0.25')
    elif (c == 4):
        print('Mochila - R$ 50.00')
    else:
        print('Código errado digitado')
