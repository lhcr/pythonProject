n=int(input('Escolha um número: '))
base=int(input('Escolha a base:\n 1-binário\n 2-octal\n 3-hexadecimal\n'))
if base==1:
    temp = format(n,"b")
    print('O valor em binário é: {} '.format(temp))
elif base==2:
    temp = format(n,"o")
    print('O valor em octal é: {} '.format(temp))
else:
    temp= format(n,"x")
    print('O valor em hexa é: {} '.format(temp))