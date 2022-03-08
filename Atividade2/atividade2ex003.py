n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print(' ')
print('1. Média entre os números digitados')
print('2. Diferença do maior pelo menor')
print('3. Produto entre os números digitados')
print('4. Divisão do primeiro pelo segundo')
op = int(input('Escolha uma das opções acima: '))
print(' ')
if (op == 1):
    op1 = (n1 + n2) / 2
    print('A média entre os números digitados é {}'.format(op1))
elif (op == 2):
    if (n1 > n2):
        print('{} > {}'.format(n1, n2))
    elif (n2 > n1):
        print('{} > {}'.format(n2, n1))
    else:
        print('Os valores são iguais')
elif (op == 3):
    op3 = n1 * n2
    print('O produto entre os números é {}'.format(op3))
elif (op == 4):
    op4 = n1 / n2
    print('A divisão do primeiro pelo segundo é {:.2f}'.format(op4))
else:
    print('ERRO')
