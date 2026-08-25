for i in range(10):
    nome=input("Digite um nome:")
    salarioBruto=float(input("Digite seu salário bruto:"))
    if(salarioBruto>=3700):
        salarioBruto*=1.225
    elif(salarioBruto>=2800):
        salarioBruto*=1.15
    elif(salarioBruto>=2200):
        salarioBruto*=1.075
    print(f"{nome} tem salário líquido igual a {salarioBruto}")