garcom='0'
SOusa=[]
while(garcom !="fim"):
    print("Digite adicionar para adicionar um item")
    print("Digite remover para remover um item")
    print("Digite fim para finalizar o programa")
    garcom=input("Escolha: Adicionar, ou remover ou fim:")
    while(garcom != 'adicionar' and garcom != 'remover' and garcom != 'fim'):
        print("Comando inválido.")
        garcom=input("DIGITE: Adicionar, ou remover ou fim:")
    if(garcom=='adicionar'):
        SOusa.append(input("Qual o nome do processo?"))
        print(SOusa)
    elif(garcom=='remover'):
        if(len(SOusa)==0):
            print("Não tem itens na lista")
        else:
            print(SOusa.pop(0))
            print(SOusa)