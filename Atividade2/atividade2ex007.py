#n = 0
#while (n >= 0):
#    n = float(input('Digite um número: '))
#    if (n >= 0):
#        print(2*n)

contador = 0
numero = int(input("Digite um número: "))
while (contador < 9 and numero >= 0):
    print(numero * 2)
    numero = int(input("Digite um número: "))
    contador += 1
print(numero*2)