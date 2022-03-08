sexo = []
for n in range(3):
    sexo.append(input("Digite o sexo (M/F): "))

m = 0
f = 0
for n in range(3):
    if (sexo[n-1] == "M"):
        m += 1
    elif (sexo[n-1] == "F"):
        f += 1

print("Há {} pessoas do sexo masculino".format(m))
print("Há {} pessoas do sexo feminino".format(f))
