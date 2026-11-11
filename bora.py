from sera import CuboPonto

class Besouro:
    def __init__(self, ponto, distancia):
        self.ponto=ponto
        self.distancia=distancia
        self.mel=[]

    #def andarMesmaFace(self, besouro, melProximo):

    def andarFaceDiferente(self, melProximo):
        dProfundidade=melProximo.y-self.ponto.y
        dHorizontal=melProximo.x-self.ponto.x
        dVertical=melProximo.z-self.ponto.z
        
        #if(self.face+melProximo.face==7):

        #else:

        #Se a face for z=10...
        if(self.ponto.face==1):
            #andar até o final do vértice
            array=self.andaReto(self.ponto.x,self.ponto.y,dHorizontal,dProfundidade)
            print("O que chega:",array)
            self.ponto.x=array[0]
            self.ponto.y=array[1]
            dHorizontal=array[2]
            dProfundidade=array[3]


            #Se x=10 ou x=0->face=3 ou 5. andaReto com y e z
            if(self.ponto.x==10 or self.ponto.x==0):
                self.ponto.face=(self.ponto.x%10)*2+3
                if(dProfundidade<0):
                    self.distancia+=2**0.5
                    array=self.andaReto(self.ponto.y-1,self.ponto.z-1,dProfundidade+1,dVertical+1)
                elif(dProfundidade>0):
                    self.distancia+=2**0.5
                    array=self.andaReto(self.ponto.y+1,self.ponto.z-1,dProfundidade-1,dVertical+1)
                else:
                    self.distancia+=2**0.5
                    array=self.andaReto(self.ponto.y,self.ponto.z-1,dProfundidade,dVertical+1)
                self.ponto.y=array[0]
                self.ponto.z=array[1]
            #y=0 ou y=10->Face=2 ou 4. andaReto com x e z
            else:
                self.ponto.face=(self.ponto.y%10)*2+2
                if(dHorizontal<0):
                    self.distancia+=2**0.5
                    array=self.andaReto(self.ponto.x-1,self.ponto.z-1,dHorizontal+1,dVertical+1)
                elif(dHorizontal>0):
                    self.distancia+=2**0.5
                    array=self.andaReto(self.ponto.x+1,self.ponto.z-1,dHorizontal-1,dVertical+1)
                else:
                    self.distancia+=1
                    array=self.andaReto(self.ponto.x,self.ponto.z-1,dHorizontal,dVertical+1)
                self.ponto.x=array[0]
                self.ponto.z=array[1]


        elif(self.ponto.face%2==1):
            array=self.andaReto(self.ponto.z,self.ponto.y,dVertical,dProfundidade)
            self.ponto.z=array[0]
            self.ponto.y=array[1]
            dVertical=array[2]
            dProfundidade=array[3]

            if(self.ponto.x==10):
                if(self.ponto.z==10):
                    self.ponto.face=1
                    if(dProfundidade<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y-1,self.ponto.x-1,dProfundidade+1,dHorizontal+1)
                    elif(dProfundidade>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y+1,self.ponto.x-1,dProfundidade-1,dHorizontal+1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.y,self.ponto.x-1,dProfundidade,dHorizontal+1)
                    self.ponto.y=array[0]
                    self.ponto.x=array[1]
                else:
                    self.ponto.face=(self.ponto.y%10)*2+2
                    if(dVertical<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z-1,self.ponto.x-1,dVertical+1,dHorizontal+1)
                    elif(dProfundidade>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z+1,self.ponto.x-1,dVertical-1,dHorizontal+1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.z,self.ponto.x-1,dVertical,dHorizontal+1)
                    self.ponto.z=array[0]
                    self.ponto.x=array[1]

            else:
                if(self.ponto.z==10):
                    self.ponto.face=1
                    if(dProfundidade<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y-1,self.ponto.x+1,dProfundidade+1,dHorizontal-1)
                    elif(dProfundidade>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y+1,self.ponto.x+1,dProfundidade-1,dHorizontal-1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.y,self.ponto.x+1,dProfundidade,dHorizontal-1)
                else:
                    self.ponto.face=(self.ponto.y%10)*2+2
                    if(dVertical<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z-1,self.ponto.x+1,dVertical+1,dHorizontal-1)
                    elif(dVertical>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z+1,self.ponto.x+1,dVertical-1,dHorizontal-1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.z,self.ponto.x+1,dVertical,dHorizontal-1)
                    self.ponto.z=array[0]
                    self.ponto.x=array[1]

        else:
            array=self.andaReto(self.ponto.z,self.ponto.x,dVertical,dHorizontal)
            self.ponto.z=array[0]
            self.ponto.x=array[1]
            dVertical=array[2]
            dHorizontal=array[3]

            if(self.ponto.y==10):
                if(self.ponto.z==10):
                    self.ponto.face=1
                    if(dHorizontal<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y-1,self.ponto.x-1,dProfundidade+1,dHorizontal+1)
                    elif(dHorizontal>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y-1,self.ponto.x+1,dProfundidade+1,dHorizontal-1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.y-1,self.ponto.x,dProfundidade+1,dHorizontal)
                    self.ponto.y=array[0]
                    self.ponto.x=array[1]
                else:
                    self.ponto.face=(self.ponto.x%10)*2+3
                    if(dVertical<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z-1,self.ponto.y-1,dVertical+1,dProfundidade+1)
                    elif(dVertical>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z+1,self.ponto.y-1,dVertical-1,dProfundidade+1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.z,self.ponto.y-1,dVertical,dProfundidade+1)
                    self.ponto.z=array[0]
                    self.ponto.x=array[1]

            else:
                if(self.ponto.z==10):
                    self.ponto.face=1
                    if(dHorizontal<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y+1,self.ponto.x-1,dProfundidade-1,dHorizontal+1)
                    elif(dHorizontal>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.y+1,self.ponto.x+1,dProfundidade-1,dHorizontal-1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.y+1,self.ponto.x,dProfundidade-1,dHorizontal)
                    self.ponto.x=array[1]
                    self.ponto.y=array[0]
                else:
                    self.ponto.face=(self.ponto.y%10)*2+2
                    if(dVertical<0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z-1,self.ponto.y+1,dVertical+1,dProfundidade-1)
                    elif(dVertical>0):
                        self.distancia+=2**0.5
                        array=self.andaReto(self.ponto.z+1,self.ponto.y+1,dVertical-1,dProfundidade-1)
                    else:
                        self.distancia+=1
                        array=self.andaReto(self.ponto.z,self.ponto.y+1,dVertical,dProfundidade-1)
                    self.ponto.z=array[0]
                    self.ponto.y=array[1]

        print("coordenadas do besouro:",self.ponto.x,self.ponto.y,self.ponto.z)
        print("coordenadas do mel", melProximo.x,melProximo.y,melProximo.z)


    def andaReto(self,CAdajacente,COposto,DAdjacente,DOposto):
        if(CAdajacente!=0 and CAdajacente!=10 and COposto!=0 and COposto!=10):
            print(CAdajacente,COposto)
            print("distancia:",self.distancia)
            if(DAdjacente>0 and DOposto>0):
                self.distancia+=2**0.5
                return(self.andaReto(CAdajacente+1,COposto+1,DAdjacente-1,DOposto-1))
            elif(DAdjacente<0 and DOposto<0):
                self.distancia+=2**0.5
                return(self.andaReto(CAdajacente-1,COposto-1,DAdjacente+1,DOposto+1))
            elif(DAdjacente>0 and DOposto<0):
                self.distancia+=2**0.5
                return(self.andaReto(CAdajacente+1,COposto-1,DAdjacente-1,DOposto+1))
            elif(DAdjacente<0 and DOposto>0):
                self.distancia+=2**0.5
                return(self.andaReto(CAdajacente-1,COposto+1,DAdjacente+1,DOposto-1))
            elif(DAdjacente>0):
                self.distancia+=1
                return(self.andaReto(CAdajacente+1,COposto,DAdjacente-1,DOposto))
            elif(DAdjacente<0):
                self.distancia+=1
                return(self.andaReto(CAdajacente-1,COposto,DAdjacente+1,DOposto))
            elif(DOposto>0):
                self.distancia+=1
                return(self.andaReto(CAdajacente,COposto+1,DAdjacente,DOposto-1))
            elif(DOposto<0):
                self.distancia+=1
                return(self.andaReto(CAdajacente,COposto-1,DAdjacente,DOposto+1))
            else:
                #Chegou ao destino->próximo Mel ou nada
                return([CAdajacente,COposto])
        else:
            #Aresta-> andar o outro coisa e mudar de face
            print("O que eu to mandando",[CAdajacente,COposto,DAdjacente,DOposto])
            return([CAdajacente,COposto,DAdjacente,DOposto])



pontoInical=CuboPonto(3, 3, 0, 5)
mel1=CuboPonto(1,5,0,3)
mel2=CuboPonto(2,8,1,10)
mel3=CuboPonto(5,10,2,5)
mel4=CuboPonto(5,10,2,7)
mel5=CuboPonto(4,9,10,2)
besouroPonto=Besouro(pontoInical, 0)

besouroPonto.mel.append(mel1)
besouroPonto.mel.append(mel2)
besouroPonto.mel.append(mel3)
besouroPonto.mel.append(mel4)
besouroPonto.mel.append(mel5)

besouroPonto.andarFaceDiferente(mel2)