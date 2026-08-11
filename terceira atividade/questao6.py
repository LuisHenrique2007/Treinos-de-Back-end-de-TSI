boi=int(input("Digite um número:"))
vaca=int(input("Digite outro número:"))
touro=int(input("Digite outro número:"))
if(boi<=vaca):
    if(touro<=boi and touro<=vaca):
        print(vaca,boi,touro)
    elif(touro>=boi and touro<=vaca):
        print(vaca,touro,boi)
    else: print(touro,vaca,boi)
elif(vaca<=boi):
    if(touro<=boi and touro<=vaca):
        print(boi,vaca,touro)
    elif(touro>=vaca and touro<=boi):
        print(boi,touro,vaca)
    else: print(touro,boi,vaca)