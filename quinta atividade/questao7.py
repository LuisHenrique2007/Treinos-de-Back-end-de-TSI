print("Quando digitar -1, o código para")
criancas=0
velhos=0
idade=int(input("Digite várias idades que diremos a quantidade de pessoas com idade menor do que 21 e maior do que 50:"))
while(idade!=-1):
    if(idade>50):
        velhos+=1
    elif(idade<21):
        criancas+=1
    idade=int(input("Digite uma idade:"))
print("a quantidade de pessoas com idade menor do que 21 é ",criancas)
print("a quantidade de pessoas com idade do que 50 é ",velhos)
