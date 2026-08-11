i=100
primos=[]
while(i>1):
    x=i-1
    teste=True
    while(x>1):
        if(i%x==0):
            teste=False
            x=0
        x-=1
    if(teste):
        primos.insert(0,i)
    i-=1
print(primos)
print(len(primos))
a=int(input("Digite um número:"))
if(a in primos):
    print('Seu número é primo')
else:
    print("Seu número não é primo")