fio=input("Digite qualquer coisa com mais de 3 caracteres: ")
while (len(fio)<4):
    print("A sitring não atingiu o tamanho mínimo necessário.")
    fio=input("Digite qualquer coisa com mais de 3 caracteres: ")


def oif(fio):
    oif=''
    for x in range(len(fio)-1,-1,-1):
        oif+=fio[x]
    return oif
print("Resposta da letra a:",oif(fio))

def f(fio):
    f=''
    for x in range(len(fio)//2):
        f+=fio[x]
    return f
print("Resposta da letra b:",f(fio))


def o(fio):
    o=''
    for x in range(len(fio)//2+len(fio)%2,len(fio)):
        o+=fio[x]
    return o
print("Resposta da letra c:",o(fio))



def of(fio):
    of=o(fio)
    of+=f(fio)
    return of
print("Resposta da letra d:",of(fio))



def iof(fio):
    iof=''
    for x in range(len(fio)):
        if(fio[x]=="a" or fio[x]=="A" or fio[x]=="e" or fio[x]=="E" or fio[x]=="i" or fio[x]=="I" or fio[x]=="o" or fio[x]=="O" or fio[x]=="u" or fio[x]=="U"):
            iof+=fio[x]
    for x in range(len(fio)):
        if(fio[x]!="a" and fio[x]!="A" and fio[x]!="e" and fio[x]!="E" and fio[x]!="i" and fio[x]!="I" and fio[x]!="o" and fio[x]!="O" and fio[x]!="u" and fio[x]!="U"):
            iof+=fio[x]
    return iof
print("Resposta da letra e:",iof(fio))


def boss(fio):
    boss=''
    for x in range(len(fio)//2):
        boss+=fio[x]
        boss+=fio[len(fio)//2+len(fio)%2+x]
    return boss
print("A resposta da letra f:",boss(fio))