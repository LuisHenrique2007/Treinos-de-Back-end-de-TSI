sport=float(input("Digite o primeiro valor:"))
santinha=float(input("Digite o segundo valor:"))
nautico=float(input("Digite o terceiro valor:"))
if(nautico*santinha<sport*nautico):
    nautico*=sport
else: nautico*=santinha
sport*=santinha
if(sport>nautico):
    print(sport)
else: print(nautico)
