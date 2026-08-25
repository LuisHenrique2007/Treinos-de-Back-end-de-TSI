mediaT=0
percentual=0
for i in range(20):
    nome=input("Digite seu nome:")
    nota=0
    for h in range(7):
        nota+=float(input("Digite sua nota:"))
    nota/=7
    print(f"O aluno {nome} obteve de média {nota}")
    mediaT+=nota
    if(nota>=5):
        percentual+=5
print("A média da turma foi: ",mediaT/20)
print("A porcentagem de alunos aprovados é ",percentual,"%")