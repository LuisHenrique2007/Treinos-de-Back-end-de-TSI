lista=[]
lista.append(float(input("Digite um número:")))
maior=lista[0]
menor=lista[0]
for i in range(14):
    lista.append(float(input("Digite um número:")))
    if(maior<lista[i+1]):
        maior=lista[i+1]
    elif(menor>lista[i+1]):
        menor=lista[i+1]
print("A lista é:",lista)
print("O maior valor é:",maior,". Que está no índice:",lista.index(maior))
print("O menor valor é:",menor,". Que está no índice:",lista.index(menor))