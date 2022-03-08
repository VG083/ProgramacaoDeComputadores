resposta = "sim"

produtos =["pao baguete", "pao doce", "tapioca", "torrada", "cafe","sonho"]

precos = [1.25,0.50,3.50,4.30,1.30,2.35]

quantidades = [0,0,0,0,0,0]

valor_total = 0

while(resposta != "nao"):

    indice_produto = int(input("Qual produto você quer?\n"

                              "0- Pão baguete: R$1,25, 1- Pão doce - R$0,50 \n"

                              "2- Tapioca: R$3,50 , 3- Torrada: R$ 4,30 \n"

                               "4- Cafe: R$1,30, 5- Sonho: R$2,35\n >  "))

    qtd = int(input("Quantidade?  "))

    quantidades[indice_produto] += qtd

    resposta=input("Quer comprar mais alguma coisa? \n"

                   "Digite qualquer coisa para continuar ou 'nao' para sair>  ")



for x in range(len(quantidades)):

    if(quantidades[x] > 5):

        print("Parabéns, você terá um desconto de 10% no produto: ", produtos[x])

        valor_total = valor_total + (quantidades[x]*precos[x])*0.9

    else:

        valor_total += quantidades[x]*precos[x]

print("Valor total é de: R$", valor_total)



for y in range(len(quantidades)):

    if(quantidades[y] > 0):

        print("Você comprou ", quantidades[y], " ", produtos[y])
