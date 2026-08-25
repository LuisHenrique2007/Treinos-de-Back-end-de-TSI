beijaFlor=input("Digite C ou c para casado; S ou s para solteiro; D ou d para divorciado:")
if(beijaFlor=='c' or beijaFlor=='C'):
    print("Você está casado")
elif(beijaFlor=='d' or beijaFlor=='D'):
    print("Você está divorciado")
elif(beijaFlor=='s' or beijaFlor=='S'):
    print("Você está solteiro")
else:
    print("Estado civil inválido")