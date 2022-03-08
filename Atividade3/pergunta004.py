numeros = []
for n in range(4):
    numeros.append(float(input("Digite um número real: ")))

positivos = 0.0
negativos = 0.0
for p in range(4):
    if (numeros[p-1] > 0):
        positivos += numeros[p-1]
    if (numeros[p-1] < 0):
        negativos += numeros[p-1]

print("Soma dos números positivos: {}".format(positivos))
print("Soma dos números negativos: {}".format(negativos))
