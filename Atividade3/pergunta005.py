valores = []
for n in range(5):
    valores.append(float(input("Digite o preço do produto: R$ ")))

acimade50 = 0
entre50e80 = 0
acima80 = 0
media = 0

for p in range(5):
    if (valores[p-1]<=49.99):
        acimade50 += 1
    elif (valores[p-1]>=50.0 and valores[p-1]<=80.0):
        entre50e80 += 1
    elif (valores[p-1] >= 80.01):
        acima80 += 1
    media += valores[p-1]
    
print("Quantidade de produtos inferior a R$ 50,00: {}".format(acima80))
print("Quantidade de produtos com preço entre R$ 50,00 e 80,00: {}".format(entre50e80))
print("Quantidade de produtos com preço acima de R$ 80,00: {}".format(acima80))
print("Média dos preços dos produtos: {:.2f}".format(media/5))