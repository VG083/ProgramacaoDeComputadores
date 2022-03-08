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

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
op = input("Digite a operação: ")
print(" ")
print(calculadora(n1,n2,op))