lista=[27]
for i in range(1, 9):
    lista.append(lista[i-1]+1)
lista.append(lista[0])
print(lista)