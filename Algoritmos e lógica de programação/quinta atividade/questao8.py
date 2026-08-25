par=0
for i in range(10):
    num=float(input("Digite um número inteiro:"))
    while(num%1!=0):
        num=float(input("Valor inválido, digite um número inteiro:"))
    if(num%2==0):
        par+=1
print("A quantidade de números pares é ",par)
print("A quantidade de úmeros ímpares é ",10-par)