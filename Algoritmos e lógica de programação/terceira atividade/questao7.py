gremio=float(input("Digite uma nota:"))
internacional=float(input("Digite uma nota:"))
juventude=float(input("Digite uma nota:"))
if(gremio>juventude and gremio>internacional):
    print((gremio*5+juventude*2.5+internacional*2.5)/10)
elif(juventude>gremio and juventude>internacional):
    print((juventude*5+gremio*2.5+internacional*2.5)/10)
else:
    print((internacional*5+gremio*2.5+juventude*2.5)/10)