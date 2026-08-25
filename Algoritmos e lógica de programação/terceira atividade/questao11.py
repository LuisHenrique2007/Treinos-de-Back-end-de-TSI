atleticoMineiro=float(input("Digite seu salário bruto:"))
cruzeiro=float(input("Digite o valor da prestação:"))
if(atleticoMineiro*0.30<cruzeiro):
    print("O empréstimo não pode ser concedido para você")
else: print("O empréstimo pode ser concedido pra você")