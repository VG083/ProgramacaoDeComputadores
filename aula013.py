# estrutura da lista
#lista1 = ["oi", "ola", "xau", 3.2]
#lista2 = [5, 3]
# operador de concatenação
#lista3 = lista1 + lista2
# remoção de elementos: remove ou pop
#lista3.remove(3.2)
#lista1.pop(len(lista1)- 1)
#print(lista3)

lista = ["Detergente", "Desinfetante", "Água Sanitária", "Sabão em pó", "Luvas", "Papel Toalha"]
print(lista)
lista[0] = "Sabão em barra"
print(lista[(len(lista)-1)])
lista.remove("Desinfetante")
lista2 = ["Esponja", "Vassoura", "Espanador"]
listanova = lista + lista2
print(listanova)

notas = []
for i in range(3):
    notas.append(float(input("Digite a nota: ")))
print(notas)
notas.append(float(input("Digite a nota: ")))
notas.append(float(input("Digite a nota: ")))
print(notas)
notas.insert(0, float(input("Digite a nota: ")))
print(notas)
notas.insert(len(notas), float(input("Digite a nota: ")))
print(notas)

nome = []
nota = []
for n in range(4):
    nome.append(input("Digite o nome do {}º aluno: ".format(n+1)))
    nota.append(input("Digite a nota do {}º aluno: ".format(n+1)))

media = 0
for m in range(len(nota)):
    media += nota[m]
media = media / len(nota)
print("A média da turma foi: {:.2f}".format(media))

if float(nota[0]) > 7:
    print("{}, parabéns pela nota".format(nome[0]))
if float(nota[1]) > 7:
    print("{}, parabéns pela nota".format(nome[1]))
if float(nota[2]) > 7:
    print("{}, parabéns pela nota".format(nome[2]))
if float(nota[3]) > 7:
    print("{}, parabéns pela nota".format(nome[3]))