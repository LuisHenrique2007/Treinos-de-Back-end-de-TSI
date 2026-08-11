portuguesa=0
botafogo=0
corinthians=int(input("Digite quantas pessoas terão no grupo:"))
mirassol=input("Qual o seu nome?")
santos=float(input("Digite sua altura:"))
portuguesa+=santos
if(santos>1.85):
    botafogo+=1
for novorizontino in range(corinthians-1):   
    palmeiras=input("Qual o seu nome?")
    saoPaulo=float(input("Digite sua altura:"))
    if(santos>saoPaulo):
        santos=saoPaulo
        mirassol=palmeiras
    portuguesa+=saoPaulo
    if(saoPaulo>1.85):
        botafogo+=1
print(f"O nome da pessoa com menor altura é {mirassol}, tendo a altura {santos}")
print(f"a média do grupo foi {portuguesa/corinthians} e a quantidade de pessoas maiores 1.85 foi {botafogo}")