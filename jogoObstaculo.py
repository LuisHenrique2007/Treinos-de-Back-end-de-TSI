import re

n=int(input("digite um número dois e dez:"))
while(n<2 or n>10):
    n=int(input("digite um número entre DOIS e DEZ:"))
decisao=9
matriz=[]
for i in range(n):
    if(decisao==1):
        linha=input(f"Digite {n} caracteres, entre S, L, T, R, M e W:")
        while(len(linha)!=n or bool(re.search(r"[^SsLlTtWwRrMm]", linha))):
            linha=input(f"Digite {n} caracteres, entre S, L, T, R, M e W:")
    elif(i==0):
        linha=input(f"Digite {n-1} caracteres, entre S, L, T, R, D, M e W:")
        while(len(linha)!=n-1 or bool(re.search(r"[^SsLlTtWwRrDdMm]", linha))):
            linha=input(f"Digite {n-1} caracteres, entre S, L, T, R,D, M e W:")
        linha="A"+linha
    else:
        linha=input(f"Digite {n} caracteres, entre S, L, T, R,D, M e W:")
        while(len(linha)!=n or bool(re.search(r"[^SsLlTtWwRrDdMm]", linha))):
            linha=input(f"Digite {n} caracteres, entre S, L, T, R,D, M e W:")
    if("d" in linha or "D" in linha):
        decisao=1
    print(linha)
    matriz.append([])
    for x in range(len(linha)):
        matriz[i].append(linha[x])

print(matriz[0])
print(matriz[1])
print(matriz[2])

for l in range(n):
    for h in range(n):
        if(matriz[l][h]=="R" or matriz[l][h]=="r"):
            saida=""
            if(l!=0 and h!=0):
                if(matriz[l-1][h-1] in "SsLlWwTt"):
                    saida+=matriz[l-1][h-1]
                if(matriz[l-1][h] in "SsLllWwTt"):
                    saida+=matriz[l-1][h]
                if(l!=n-1 and h!=n-1):
                    if(matriz[l+1][h+1] in "SsLlWwTt"):
                        saida+=matriz[l+1][h+1]
                    if(matriz[l-1][h+1] in "SsLlWwTt"):
                        saida+=matriz[l-1][h+1]
                    if(matriz[l+1][h] in "SsLlWwTt"):
                        saida+=matriz[l+1][h]
                    if(matriz[l+1][h-1] in "SsLlWwTt"):
                        saida+=matriz[l+1][h-1]
            elif(l!=0):
                if(matriz[l-1][h] in "SsLlWwTt"):
                    saida+=matriz[l-1][h]
                if(h!=n-1):
                    if(matriz[l-1][h+1] in "SsLlWwTt"):
                        saida+=matriz[l-1][h+1]
                if(l!=n-1):
                    if(matriz[l+1][h] in "SsLlWwTt"):
                        saida+=matriz[l+1][h]
                    if(h!=0):
                        if(matriz[l+1][h-1] in "SsLlWwTt"):
                            saida+=matriz[l+1][h-1]
            if(h!=0):
                if(matriz[l][h-1] in "SsLlWwTt"):
                    saida+=matriz[l][h-1]
                if(h!=n-1):
                    if(matriz[l][h+1] in "SsLlWwTt"):                    
                        saida+=matriz[l][h+1]
            print(saida)
        elif(matriz[l][h]=="D" or matriz[l][h]=="d"):
            print("DESTINO")
            break
print(n)
