r = 'sim'
while (r != 'nao'):
    if (r == 'sim'):
        d = float(input('Digite a distância percorrida pelo atleta: '))
        t = float(input('Digite o tempo que levou para percorrer a distância: '))
        print('A velocidade média do atleta foi {}'.format(d/t))
    else:
        print('Resposta inválida')
    r = input('Deseja continuar usando o programa? (sim/nao) ')
