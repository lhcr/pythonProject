totgasto = maMil = maBarato = valProd = 0
print('-------Super do Pobre--------\n')
while True:
    nomeProd= str(input('Informe o nome do produto: '))
    valorProd=  float(input('Informe o valor: '))
    totgasto+=valorProd
    if maBarato==0:
        maBarato = valorProd
        nProdBara = nomeProd
    elif maBarato>valorProd:
        maBarato = valorProd
        nProdBara = nomeProd
    if valorProd>1000:
        maMil+=1
    pergunta = str(input('Deseja continuar? '))
    if pergunta in 'nN':
        break
    
print(f'{maMil} custaram mais de mil reais\no produto mais barato foi o {nProdBara} e custou {maBarato}\nTotal gasto {totgasto} ')
    


