valSacar= int(input('Que valor deseja sacar? '))
cinc = vin = dez = um = 0

while valSacar>=50:
    valSacar-=50
    cinc+=1
while valSacar>=20:
    valSacar-=20
    vin+=1
while valSacar>=10:
    valSacar-=10
    dez+=1
while valSacar>=1:
    valSacar-=1
    um+=1
print(f'São {cinc} notas de R$50\n{vin} notas de R$20\n{dez} nota de R$10\n{um} nota de R$1 ')
