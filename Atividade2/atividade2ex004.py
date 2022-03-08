s = float(input('Digite o salário: R$ '))
if (s < 300):
    print('O novo salário será de R$ {:.2f}'.format(1.45*s))
elif (s <= 600):
    print('O novo salário será de R$ {:.2f}'.format(1.25*s))
else:
    print('O novo salário será de R$ {:.2f}'.format(1.15*s))
