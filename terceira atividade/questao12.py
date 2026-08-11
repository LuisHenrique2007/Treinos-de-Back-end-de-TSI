paysandu=int(input("Informe sua idade:"))
if(paysandu<19):
    paysandu=int(input("Você vai querer o plano enfermaria ou apartamento? Digite 1 pra enfermaria; Digite 0 pra apartamento:"))
    if(paysandu==1):
        paysandu=400
    else:
        paysandu=490
elif(paysandu<40):
    paysandu=int(input("Você vai querer o plano enfermaria ou apartamento. Digite 1 pra enfermaria; Digite 0 pra apartamento:"))
    if(paysandu==1): 
        paysandu=520
    else:paysandu=610
elif(paysandu<60):
    paysandu=int(input("Você vai querer o plano enfermaria ou apartamento. Digite 1 pra enfermaria; Digite 0 pra apartamento:"))
    if(paysandu==1):
        paysandu=640
    else: paysandu=740
else:
    paysandu=int(input("Você vai querer o plano enfermaria ou apartamento. Digite 1 pra enfermaria; Digite 0 pra apartamento:"))
    if(paysandu==1):
        paysandu=760
    else: paysandu= 890
paysandu+=int(input("Você vai querer o plano odontológico? Digite 1 pra sim; Digite 0 pra não:"))*30
print(paysandu)