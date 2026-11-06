from elementoArco import ElementoArco

class listaCircular:
    def __init__(self, primeiro):
        self.primeiro=primeiro
    
    def printListaCircular(self):
        if(self.primeiro!=None):
            correCirculo=self.primeiro
            print(correCirculo.valor)
            correCirculo=correCirculo.proximo
            while(correCirculo!=self.primeiro):
                print(correCirculo.valor)
                correCirculo=correCirculo.proximo
        else:
            print("Não tem nada na lista")
            
    def printListaCircularInversa(self):
        if(self.primeiro!=None):
            correCirculo=self.primeiro.anterior
            print(correCirculo.valor)
            correCirculo=correCirculo.anterior
            while(correCirculo!=self.primeiro.anterior):
                print(correCirculo.valor)
                correCirculo=correCirculo.anterior
        else:
            print("Não tem elemento na lista")
    
    def addElementoInicio(self, e):
        oldFirst=self.primeiro
        if(oldFirst!=None):
            novato=ElementoArco(e,oldFirst,oldFirst.anterior)
            oldFirst.anterior, novato.anterior.proximo=novato, novato
        else:
            novato=ElementoArco(e,None,None)
            novato.proximo, novato.anterior=novato, novato
        self.primeiro=novato
    
    def addElementoFinal(self, e):
        first=self.primeiro
        if(first!=None):
            novato=ElementoArco(e,first,first.anterior)
            first.anterior, novato.anterior.proximo=novato, novato
        else:
            novato=ElementoArco(e,None,None)
            novato.proximo, novato.anterior=novato, novato
        self.primeiro.anterior=novato
    
    def removerElementoInicio(self):
        if(self.primeiro!=None):
            if(self.primeiro!=self.primeiro.proximo):
                excluido=self.primeiro
                self.primeiro=excluido.proximo
                self.primeiro.anterior=excluido.anterior
                excluido.anterior.proximo=self.primeiro
                del(excluido)       
            else:
                first=self.primeiro
                self.primeiro=None
                del(first)    
        else:
            print("Não existe elemento na lista")
    
    def removerElementoFinal(self):
        if(self.primeiro!=None):
            if(self.primeiro.proximo!=self.primeiro):
                excluido=self.primeiro.anterior
                self.primeiro.anterior=excluido.anterior
                excluido.anterior.proximo=excluido.proximo
                del(excluido)
            else:
                first=self.primeiro
                self.primeiro=None
                del(first)    
        else:
            print("Não existe elemento na lista")
    
    def removerQualquerElemento(self, e):
        if(self.primeiro!=None):
            correCirculo = self.primeiro.proximo
            if(self.primeiro.valor==e):
                self.removerElementoInicio()
            elif(self.primeiro.proximo==None):
                print("Não tem ",e,"na lista")
            else:
                while(correCirculo.valor != e and self.primeiro!=correCirculo):
                    correCirculo=correCirculo.proximo
                if(correCirculo.valor==e):
                    excluido=correCirculo
                    correCirculo=excluido.anterior
                    correCirculo.proximo=excluido.proximo
                    excluido.proximo.anterior=correCirculo
                    del(excluido)
                else:
                    print("Não tem", e," na lista")
        else:
            print("a lista tá vazia")


lista=listaCircular(None)
lista.addElementoInicio(1)
lista.addElementoInicio(5)
lista.addElementoFinal(10)
lista.addElementoFinal(800)
print("\n5,1,10,800")
lista.printListaCircular()

print("\n800,10,1,5")
lista.printListaCircularInversa()

lista.removerQualquerElemento(1)
lista.removerQualquerElemento(9)
lista.removerQualquerElemento(5)
lista.removerQualquerElemento(5)
lista.removerQualquerElemento(10)
lista.removerQualquerElemento(20)
lista.removerQualquerElemento(800)
lista.removerQualquerElemento(3231)

lista.printListaCircular()
lista.printListaCircularInversa()