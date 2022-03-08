#funções = subrotinas
#a função é um algoritmo que roda dentro do programa
# def nomedafunção(parâmetro)
#   códigosdafunção
#
# https://www.pythonprogressivo.net/2018/06/Calculadora-Python-Funcoes.html

def calculadora(n1,n2,op):
    if(op == "+"):
        return n1+n2
    elif(op == "-"):
        return n1-n2
    elif(op == "*"):
        return n1*n2
    elif(op == "/"):
        if(n2 != 0):
            return n1/n2
        else:
            print("Divisão por 0 não é permitida")
    else:
        print("Operador inválido")

numero1 = float(input("Numero1> "))
numero2 = float(input("Numero2> "))
simbolo = input("Digite o operador> ")
print(calculadora(numero1,numero2,simbolo))

def media(num1, num2, num3):
    m = (num1+num2+num3) / 3
    if (m>=7):
        return "Aprovado"
    elif (m<7):
        return "Reprovado"

a = media(7, 8, 9)
print(a)

def func(num1, num2):
    return num1**2, num2**2

a, b = func(2, 3)
print(a)
print(b)

def eh_par(num):
    if (num % 2 == 0):
        return True
    else:
        return False

numero = int(input("Digite um número: "))
print(eh_par(numero))

def soma(num1, num2):
    valor = num1+num2
    return valor

a = soma(5,7)
print(a)

def calcula_imc(peso,altura):
    res = peso/pow(altura,2)
    return res

a = calcula_imc(75, 1.78)
print(a)

def potencia(num1, num2):
    resultado = 1
    for a in range(num2):
        resultado *= num1
    return resultado

def meuNome (nome):
    print("Eu sou: ", nome)

meuNome("Douglas")

a = potencia(2, 3)
print(a)
