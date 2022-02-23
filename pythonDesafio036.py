vc=float(input('Valor da casa: '))
sal=float(input('Salário: '))
anos=int(input('Em quantos anos vai pagar: '))
prest=vc/(12*anos)
if prest>=sal+sal*0.3:
    print('Empréstimo negado')
else:
    print('Você conseguiu o empréstimo.')
