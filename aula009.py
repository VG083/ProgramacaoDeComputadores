n = int(input('Digite um número: '))
contador = 0
while (n != 0):
    if (n == 2):
        contador += 1
    n = int(input('Digite outro número: '))
print('O número 2 foi digitado {} vezes'.format(contador))
