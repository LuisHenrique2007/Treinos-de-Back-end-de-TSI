num=float(input("Digite sua nota:"))
while(num < 0 or num > 10):
    num=float(input("Valor inválido, digite sua nota:"))
if(num>=7):
    print("Você tá aprovado")
else: print("Você está reprovado")