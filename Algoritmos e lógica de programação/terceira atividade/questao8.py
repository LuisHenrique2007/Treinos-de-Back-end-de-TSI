letra=input("Digite seu turno: m ou M para matutino, v ou V para vespertino, n ou N par noturno:")
if(letra=="m" or letra=="M"):
    print("Bom dia!")
elif(letra=="v" or letra=="V"):
    print("Boa tarde!")
elif(letra=="n" or letra=="N"):
    print("Boa noite!")
else: print("Valor inválido")