dados = []
pessoas = []
maPesadas = []
mePesadas= []
cad = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[cad])

    if cad == 0:
        mePesadas.append(pessoas[0])
        maPesadas.append(pessoas[cad])
    else:
        if dados[cad][1] > maPesadas[0][1]:
            maPesadas.clear()
            mePesadas.append(dados[cad])
        elif dados[cad][1] < mePesadas[0][1]:
            mePesadas.clear()
            mePesadas.append(dados[cad])
        
    cad+=1
    continuar = str(input('Continuar?[S/N] '))
    if continuar in 'nN':
        break
print(f'Pessoas {dados[0]}\nMenor peso {mePesadas}\nMaior peso {maPesadas}')