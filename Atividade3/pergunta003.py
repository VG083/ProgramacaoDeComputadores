opiniao = []
for n in range(5):
    opiniao.append(int(input("Digite 1 para regular, 2 para bom e 3 para ótimo: ")))

otimo = 0
bom = 0
regular = 0

for op in range(5):
    if ((opiniao[op-1]) == 1):
        regular += 1
    elif ((opiniao[op-1]) == 2):
        bom += 1
    elif ((opiniao[op-1]) == 3):
        otimo += 1

print("{} pessoas acharam o filme ótimo".format(otimo))
print("{} pessoas acharam o filme bom".format(bom))
print("{} pessoas acharam o filme regular".format(regular))
