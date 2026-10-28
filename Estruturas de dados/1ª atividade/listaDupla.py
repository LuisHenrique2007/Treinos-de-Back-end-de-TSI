from elementoDuplo import ElementoDuplo

class ListaDupla:
    def __init__(self,primeiro):
        self.primeiro = primeiro
        
    ##def printListaDuplaInversa():

    def printLista(self):
        correInicio=self.primeiro
        while(correInicio!=None):
            print(correInicio.valor)
            correInicio=correInicio.proximo
        
    def addElementoFinal(self,numero):
        first=self.primeiro
        if(first!=None):
            while(first.proximo!=None):
                first=first.proximo
            e=ElementoDuplo(numero,None)
            first.proximo=e
        else:
            e=ElementoDuplo(numero,None)
            self.primeiro=e
            
            
    def addElementoInicio(self,numero):
        first=self.primeiro
        if(first!=None):
            e=ElementoDuplo(numero,first)
            self.primeiro=e
        else:
            e=ElementoDuplo(numero,None)
            self.primeiro=e
            
    def removerElementoInicio(self):
        first=self.primeiro
        if(first!=None):
            self.primeiro=self.primeiro.proximo
            del(first)
        else:
            print("NÃO TEM NADA, IDIOTAAAA")
            
    def removerElementoFinal(self):
        first=self.primeiro
        if(first!=None):
            if(first.proximo!=None):
                while(first.proximo.proximo!=None):
                    first=first.proximo
                del(first.proximo)
                first.proximo=None
            else:
                self.primeiro=None
                del(first)
            
        else:
            print("NÃO TEM NADA, IDIOTAAAA")
            
    def removerQualquerElemento(self, e):
        first=self.primeiro
        if(first!=None):
            if(first.valor==e):
                self.removerElementoInicio()
            elif(first.proximo==None):
                print("Não tem ",e," na lista")
            else:
                excluido=first
                excluido=first.proximo
                while(excluido.valor != e and excluido.proximo != None):
                    first=first.proximo
                    excluido=excluido.proximo
                if(excluido.valor == e):
                    first.proximo=excluido.proximo
                    del(excluido)
                else:
                    print("Não tem ",e," na lista")
        else:
            print("Não tem nada")
        

lista=ListaDupla(None)

lista.addElementoFinal(3)
lista.addElementoFinal(4)
lista.addElementoInicio(2)
lista.addElementoInicio(1)
print("1,2,3,4:")
lista.printLista()

lista.removerQualquerElemento(3)
lista.removerElementoFinal()
lista.removerElementoInicio()
print("\n2:")
lista.printLista()

'''
Trabalho de estrutura de dados:
Transformar os métodos de uma lista encadeada simples para
os métodos de uma lista encadeada dupla.

Próximo commit:
1. Está faltando o (atributo anterior[elementoDuplo] e o atributo final[listaDupla])
2. fazer função imprimir toda a lista só que inversa
'''