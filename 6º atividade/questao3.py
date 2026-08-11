lista=[]
par=[]
impar=[]
for i in range(4):
    lista.append(int(input("Digite um número inteiro:")))
    if(lista[i]%2==1):
        impar.append(lista[i])
    else:
        par.append(lista[i])
print("A lista por completo é:", lista)
print("Somente os ímpares da lista são:",impar)
print("Somente os pares é da lista são:",par)