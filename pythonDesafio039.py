from datetime import date


idade=int(input('Informe idade: '))
if idade<18:
    print('Moleque, falta {} anos'.format(18-idade))
elif idade>18:
    print('Velho, passou {} anos'.format(idade-18))
else:
    print('Bem vindo soldado')