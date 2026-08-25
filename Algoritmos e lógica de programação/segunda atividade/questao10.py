numero=int(input("digite um número de 3 algarismos:"))
henrique=numero-numero%10-(numero//100)*100
henrique+=(numero%10)*100+numero//100
print(henrique)