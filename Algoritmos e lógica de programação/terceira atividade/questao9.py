petrolina=float(input("Digite sua nota:"))
juazeiro=float(input("Digite sua nota:"))
print("sua notas parciais são ", petrolina, " e ", juazeiro )
petrolina=(petrolina+juazeiro)/2
print("Ou seja: sua média foi:", petrolina)
if(petrolina>=9):
   print("O conceito foi A")
   print("Então você tá aprovado")
elif(petrolina>=7.5):
   print("O conceito foi B")
   print("Então você tá aprovado")
elif(petrolina>=6):
    print("O conceito foi C")
    print("Então você tá aprovado")
elif(petrolina>=4):
    print("O conceito foi D")
    print("Então você tá reprovado")
else:
    print("O conceito foi E")
    print("Então você tá reprovado")