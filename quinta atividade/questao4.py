base=int(input("Digite um número natural para ser a base:"))
expoente=int(input("Digite um número natural para ser o expoente:"))
valor=1
while(base<0 or expoente<0):
    base=int(input("Digite um número natural para ser a base:"))
    expoente=int(input("Digite um número natural para ser o expoente:"))
if(base==0 and expoente==0):
    valor="Indeterminação"
while(expoente>0):
    valor*=base
    expoente-=1
print("O resultado da potenciação é ",valor)