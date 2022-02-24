s=0
for c in range(0,7):
    ano=int(input('Ano: '))
    idade=2022-ano
    if idade>=21:
        s=s+1
        print('idade: {}'.format(idade))
print('s: {}'.format(s))