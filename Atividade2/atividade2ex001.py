idade = int(input('Insira sua idade: '))
while (idade >= 5 and idade <= 25):
    if idade <= 10:
        print('Você pertence a Categoria Infantil')
    elif idade <= 15:
        print('Você pertence a Categoria Juvenil')
    elif idade <= 20:
        print('Você pertence a Categoria Júnior')
    elif idade <= 25:
        print('Você pertence a Categoria Profissional')
    idade = int(input('Insira sua idade: '))