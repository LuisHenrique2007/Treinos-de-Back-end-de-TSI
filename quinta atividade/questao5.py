print("Se você digitar 0, encerrará o programa")
nota=float(input("Digite sua nota:"))
media=0
tudo=0
while(nota!=0):
    tudo+=1
    media+=nota
    nota=float(input("Digite sua nota:"))
if(tudo==0):
    print("Média do quê?")
else: print("A média é",media/tudo)