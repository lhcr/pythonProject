vc=float(input('Valor da casa: '))
sal=float(input('Salário: '))
anos=int(input('Em quantos anos vai pagar: '))
prest=vc/(12*anos)
cond=sal+sal*0.3
if prest>=cond:
    print('Empréstimo negado, {} e {}'.format(prest,cond))
else:
    print('Você conseguiu o empréstimo.')
