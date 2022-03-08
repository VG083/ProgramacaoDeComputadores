n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1+n2+n3) / 3
if (m>= 5):
    print('Sua nota foi {:.1f}'.format(m))
    print('Você foi aprovado')
else:
    print('Sua nota foi {:.1f}'.format(m))
    print('Você foi reprovado')
