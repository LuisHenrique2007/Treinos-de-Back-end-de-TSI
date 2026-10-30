from elementoDuplo import ElementoDuplo

class ListaDupla:
    def __init__(self,primeiro, ultimo):
        self.primeiro = primeiro
        self.ultimo = ultimo
        
    def printListaDuplaInversa(self):
        #A lista é percorrida do início imprimindo o valor de cada item e andando para a anterior.
        correFinal=self.ultimo
        while(correFinal!=None):
            print(correFinal.valor)
            correFinal=correFinal.anterior

    def printListaDupla(self):
        #A lista é percorrida imprimindo o valor de cada item e andando para a posterior:
        correInicio=self.primeiro
        while(correInicio!=None):
            print(correInicio.valor)
            correInicio=correInicio.proximo


        
    def addElementoFinal(self,numero):
        correFinal = self.ultimo
        #correFinal=None; quando a lista for vazia. Mas se a lista não for vazia, correFinal é um elemento.
        e=ElementoDuplo(numero,None,correFinal)
        #Se a lista não for vazia, então o último item antigo apontará ao novo último item como próximo.
        if(correFinal!=None):
            correFinal.proximo=e
        #Senão 'e' é o primeiro item da lista e o último.
        else:
            self.primeiro=e
        self.ultimo=e
            
            
    def addElementoInicio(self,numero):
        correInicio=self.primeiro
        #correFinal=None; quando a lista for vazia. Mas se a lista não for vazia, correFinal é um elemento.
        e=ElementoDuplo(numero,correInicio,None)
        #Se a lista não for vazia, então o primeiro item antigo apontará ao novo primeiro item como anterior.
        if(correInicio!=None):
            correInicio.anterior=e
        #Senão 'e' é o primeiro e o último elemento
        else:
            self.ultimo=e
        self.primeiro=e
            
    def removerElementoInicio(self):
        correInicio=self.primeiro
        #Se a lista não for vazia, então o primeiro item é o segundo, porque o primeiro item é deletado da existência
        if(correInicio!=None):
            self.primeiro=self.primeiro.proximo
            #Se a lista tiver segundo item, então o anterior dele é None
            if(self.primeiro!=None):
                self.primeiro.anterior=None
            #Senão o último também é None, já que nenhum elemento existe mais
            else:
                self.ultimo=None
            del(correInicio)
        else:
            print("NÃO TEM NADA, IDIOTAAAA")
            
    def removerElementoFinal(self):
        correFinal=self.ultimo
        #Se a lista não for vazia, então o último item é o penúltimo, porque o último item é deletado da existência
        if(correFinal!=None):
            self.ultimo=self.ultimo.anterior
            #Se a lista tiver penúltimo item, então o próximo dele é None
            if(self.ultimo != None):
                self.ultimo.proximo=None
            #Senão o último também é None, já que nenhum elemento existe mais
            else:
                self.primeiro=None
            del(correFinal)
        else:
            print("NÃO TEM NADA, IDIOTAAAA")
            
    def removerQualquerElemento(self, e):
        correInicio=self.primeiro
        correFinal=self.ultimo
        #A variável que será excluída é excluidoInicio ou excluidoFinal
        #Se a lista não for vazia, então tem algo
        if(correInicio!=None):
            #Invocar removerElementoInicio se o 'e' estiver no início 
            if(correInicio.valor==e):
                self.removerElementoInicio()
            #Testa se há mais de dois itens na lista, porque o código a seguir necessita de pelo menos 3 itens na lista.
            elif(correInicio.proximo==None or correInicio.proximo==correFinal):
                print("Não tem ",e," na lista")
            #Invocar removerElementoFinal se o 'e' estiver no final 
            elif(correFinal.valor==e):
                self.removerElementoFinal()
            else:
                #Há 2 pares de variáveis, um vindo do início, e outro vindo do final.
                #Se a quantidade de itens da lista for par, então quando os excluidos passarem entre si, estão a um item de distância um do outro; Ex: 1,2(EF e CI),3(EI e CF),4
                #Se a quantidade de itens da lista for ímpar, então quando os excluidos passarem entre si, estão a dois itens de distância um do outro; Ex: 1,2(EF),3(CF e CI),4(EI),5
                excluidoInicio=correInicio.proximo
                excluidoFinal=correFinal.anterior
                while(excluidoInicio.valor != e and excluidoFinal.valor !=e and excluidoFinal.proximo != excluidoInicio.anterior and excluidoInicio.anterior != excluidoFinal):
                    correInicio = correInicio.proximo
                    excluidoInicio = excluidoInicio.proximo

                    excluidoFinal = excluidoFinal.anterior
                    correFinal=correFinal.anterior
                    #Quando achar 'e', então o item anterior de 'e' aponta para o posterior de 'e'; o item posterior de 'e' aponta para o anterior de 'e'
                    #EXCLUIR 'e'
                if(excluidoInicio.valor == e):
                    correInicio.proximo=excluidoInicio.proximo
                    correInicio=excluidoInicio.proximo
                    correInicio.anterior=excluidoInicio.anterior
                    del(excluidoInicio)

                elif(excluidoFinal.valor == e):
                    correFinal.anterior=excluidoFinal.anterior
                    correFinal=excluidoFinal.anterior
                    correFinal.proximo=excluidoFinal.proximo
                    del(excluidoFinal)
                else:
                    print("Não tem ",e," na lista")
        else:
            print("Não tem nada")
        

lista=ListaDupla(None,None)

lista.addElementoFinal(3)
lista.addElementoFinal(4)
lista.addElementoInicio(2)
lista.addElementoInicio(1)
print("1,2,3,4:")
lista.printListaDupla()
print("\n4,3,2,1:")
lista.printListaDuplaInversa()

lista.removerQualquerElemento(2)
lista.removerElementoFinal()
lista.removerElementoInicio()
print("\n3:")
lista.printListaDuplaInversa()
lista.printListaDupla()

