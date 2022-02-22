d=float(input('Distâncai da viagem em Km: '))
if d<=200:
	print('Valor da viagem R${}'.format(d*0.50))
else:
	print('Valor da viagem R${}'.format(d*0.45))