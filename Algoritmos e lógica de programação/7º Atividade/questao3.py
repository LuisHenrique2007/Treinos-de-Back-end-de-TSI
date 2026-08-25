def primao(number):
    defesa=True
    x=number-1
    if(number>1):
        while(x>1):
            if(number%x==0):
                print("Esse número não é primo")
                defesa=False
                x=-122
            x-=1
    else:
        print("Esse número não é primo")
        defesa=False
    if(defesa!=False):
        print("Esse número é primo")
n=int(input("Digite um número:"))
primao(n)