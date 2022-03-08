p = float(input('Digite o valor do produto: R$ '))
print(' ')
print('Novo preço: ')
if (p < 50):
    print('R$ {:.2f}'.format(1.05*p))
elif (p <= 100):
    print('R$ {:.2f}'.format(1.10*p))
else:
    print('R$ {:.2f}'.format(1.15*p))
print('Classificação: ')
if (p < 80):
    print('Barato')
elif (p <= 120):
    print('Normal')
elif (p <= 200):
    print('Muito caro')
