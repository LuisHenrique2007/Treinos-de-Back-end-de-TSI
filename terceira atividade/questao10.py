gato=input("Digite um nome:")
beijaFlor=input("Digite C ou c para casado; S ou s para solteiro; D ou d para divorciado:")
jabuti=int(input("Digite uma idade:"))
if(beijaFlor=='c' or beijaFlor=='C' and jabuti<25):
    print(gato," ACEITA")
elif(beijaFlor=='d' or beijaFlor=='D' or beijaFlor=='s' or beijaFlor=='S'):
    print(gato, "NÃO ACEITA")
else:
    print("Estado civil inválido")