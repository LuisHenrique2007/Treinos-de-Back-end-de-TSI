num=int(input("Digite um número positivo:"))
while(num<=0):
    num=int(input("Digite um número POSITIVO:"))
tudo=1
while(num//tudo>10):
    tudo*=10
i=1
while(tudo/i>=i):
    num+=((num//(tudo/i))%10)*i-(num%(i*10)-num%i)+((num%(i*10)-num%i)/i)*(tudo/i)-(num//(tudo/i)%10)*(tudo/i)
    i*=10
print(num)