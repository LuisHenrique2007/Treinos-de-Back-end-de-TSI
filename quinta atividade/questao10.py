print("Quando digitar um número menor que 1, o programa encerrará")
numero=int(input("Digite um número inteiro que diremos o fatorial dele:"))
while(numero>=1):
    resultado=1
    while(numero>1):
        resultado*=numero
        numero-=1
    print("O fatorial desse número é ", resultado)
    numero=int(input("Digite um número inteiro que diremos o fatorial dele:"))