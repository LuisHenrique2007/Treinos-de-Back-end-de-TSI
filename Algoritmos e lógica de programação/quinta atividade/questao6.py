print("Se você digitar -1, encerrará o programa")
num=float(input("Informe um número que diremos quantos números entre 100 e 200 você digitou:"))
tudo=0
while(num!=-1):
    if(num>100 and num<200):
        tudo+=1
    num=float(input("Informe um número:"))
print("a quantidade de números entre 100 e 200 que você digitou foi: ",tudo)