entrada=input("Quer comprar ingresso(Sim ou Não)?")
valorFinal=0

while(entrada!="Não" or entrada=="Sim"):
    if(entrada=="Sim"):


        entrada=input("Qual a categoria(A|B|C)?")
        while(entrada!="A" and entrada!="B" and entrada!="C"):
            entrada=input("Qual a categoria(A|B|C)?")
        if(entrada=="A"):
            ingresso=40
        elif(entrada=="B"):
            ingresso=30
        else:
            ingresso=25


        ingresso*=int(input("Qual a quantidade?"))

        entrada=int(input("Qual a idade?"))
        if(entrada>60):
            ingresso/=2

        valorFinal+=ingresso
        print("O valor total deu",valorFinal)
    else: 
        print("valor inválido")
    entrada=input("Quer comprar ingresso(Sim ou Não)?")