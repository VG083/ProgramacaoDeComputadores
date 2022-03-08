# OBS: os dois alunos precisam enviar!
# Faça um programa para uma padaria utilizando lista:
# Receba um produto por vez e a quantidade dele
# O usuário deve informar quando não quiser comprar mais nada
# Calcule o valor total e apresente a lista de produtos e quantidades compradas
# Se ele tiver comprado mais de 5 unidades de um produto, deve receber um desconto de 10% nele (e ser avisado sobre isso)
# PRODUTOS:
# Pão baguete - R$1,25 Torrada - R$ 4,30
# Pão doce - R$0,50 Café - R$1,30
# Tapioca - R$3,50 Sonho - R$ 2,35
resposta = "sim"
produtos = ["pao baguete", "pao doce", "tapioca", "torrada", "cafe", "sonho"]
precos = [1.25, 0.50, 3.50, 4.30, 1.30, 2.35]
quantidade = [0, 0, 0, 0, 0, 0]
while (resposta != "nao"):
    indice_produto = int(input("Qual produto você quer?\n"
    "0- Pão baquete: 1,25 ; 1- Pão doce: 0,50\n"
    "2- Tapioca: 3,50 ; 3- Torrada: 4,50\n"
    "4- Café: 1,30 ; 5- Sonho: 2,35\n > "))
    qtd = int(input("Quantidade? "))
    quantidade[indice_produto] += qtd
    resposta = input("Quer comprar mais alguma coisa? \n"
    "Digite qualquer coisa para continuar ou 'nao' para sair> ")

valor_total = 0
for x in range(len(quantidade)):
    if(quantidade[x] > 5):
        print("Você terá desconto de 10%")
        valor_total = valor_total + quantidade[x]*precos[x]*0.9
    else:
        valor_total += quantidade[x]*precos[x]
print("Valor total: R$ {:.2f}".format(valor_total))

for y in range(len(quantidade)):
    if(quantidade>0):
        print("Você comprou: ", quantidade[y], " ", produtos[y])
    