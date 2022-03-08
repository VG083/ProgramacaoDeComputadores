p = 0
for c in range(0,10,1):
    pn = float(input('Digite o valor do produto: R$ '))
    if (pn > p):
        p = pn
print('O produto mais caro foi de: R$ {}'.format(p))