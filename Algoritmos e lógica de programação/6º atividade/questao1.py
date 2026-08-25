linha=[]
coluna=[]
for i in range(15):
    temporario=int(input("Digite um número para primeira lista:"))
    while(temporario in linha):
        temporario=int(input("Digite outro número para primeira lista, aquele já existe:"))
    linha.append(temporario)
for i in range(15):
    temporario=int(input("Digite um número para segunda lista:"))
    while(temporario in coluna):
        temporario=int(input("Digite outro número para segunda lista, aquele já existe:"))
    coluna.append(temporario)
temporario=0
for i in range(15):
    if(coluna[temporario] in linha):
        temporario+=1
    else:
        del coluna[temporario]
print("O conjunto de interseção é ",coluna)