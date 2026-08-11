livros=[]
temporario=[]
for x in range(20):
    livros.append(input("Digite um livro:"))
i=0
while(i==0):
    favorito=input("Qual é o seu livro favorito?")
    if(favorito in livros):
        i+=1
i=0
while(i==0):
    if(livros[len(livros)-1]==favorito):
        i+=1
        del livros[len(livros)-1]
        for x in range(len(temporario)):
            livros.append(temporario.pop(len(temporario)-1))
    else:
        temporario.append(livros.pop(len(livros)-1))
print(livros)
print(favorito)