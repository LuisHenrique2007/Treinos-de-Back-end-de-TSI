atleticoMineiro=float(input("Digite o valor da hora aula:"))
atleticoMineiro*=float(input("Digite o total de aulas dadas no mês:"))
atleticoMineiro*=1-float(input("Digite o valor de desconto do INSS:"))/100
print("O valor do salário líquido é:",atleticoMineiro)