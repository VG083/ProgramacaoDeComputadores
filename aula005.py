s = float(input('Digite o salário: '))
if (s <= 300):
    print('O novo salário é: R$ {}'.format(1.35*s))
else:
    print('O novo salário é: R$ {}'.format(1.15*s))
