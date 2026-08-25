fio=input("Digite qualquer coisa com mais de 3 caracteres: ")
while (len(fio)<4):
    print("A sitring não atingiu o tamanho mínimo necessário.")
    fio=input("Digite qualquer coisa com mais de 3 caracteres: ")

print("Resposta da letra a:",fio[::-1])
print("Resposta da letra b:",fio[:len(fio)//2])
print("Resposta da letra c:",fio[len(fio)//2+len(fio)%2:])
print("Resposta da letra d:",fio[len(fio)//2+len(fio)%2:]+fio[:len(fio)//2])




iof=''
for x in range(len(fio)):
    if(fio[x]=="a" or fio[x]=="A" or fio[x]=="e" or fio[x]=="E" or fio[x]=="i" or fio[x]=="I" or fio[x]=="o" or fio[x]=="O" or fio[x]=="u" or fio[x]=="U"):
        iof+=fio[x]
for x in range(len(fio)):
    if(fio[x]!="a" and fio[x]!="A" and fio[x]!="e" and fio[x]!="E" and fio[x]!="i" and fio[x]!="I" and fio[x]!="o" and fio[x]!="O" and fio[x]!="u" and fio[x]!="U"):
        iof+=fio[x]
print("Resposta da letra e:",iof)



boss=''
for x in range(len(fio)//2):
    boss+=fio[x]
    boss+=fio[len(fio)//2+len(fio)%2+x]
print("A resposta da letra f:",boss)