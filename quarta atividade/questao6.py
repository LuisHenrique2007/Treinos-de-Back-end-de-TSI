n=int(input("Digite quantos valores terá para sabermos o maior dentre eles:"))
atleticoMineiro=0
for i in range(n):
    cruzeiro=int(input("Digite um número inteiro positivo:"))
    if(atleticoMineiro<cruzeiro):
        atleticoMineiro=cruzeiro
print(atleticoMineiro)