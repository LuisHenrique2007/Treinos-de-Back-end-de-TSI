def primao(number):
    defesa=True
    x=number-1
    if(number>1):
        while(x>1):
            if(number%x==0):
                defesa=False
                x=-122
            x-=1
    else:
        defesa=False
    return defesa
number=int(input("Digite um número:"))
if(primao(number)):
    print("Esse número é primo.")
else:
    print("Esse número não é primo.")