numeros = []
for n in range(6):
    numeros.append(int(input("Digite um número inteiro: ")))

for p in range(6):
    if (numeros[p-1] > 0):
        print(numeros[p-1])
