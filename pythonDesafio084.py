from calendar import c


dados = []
pessoas = []
maPesadas = []
mePesadas= []
cad = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    if cad == 0:
        mePesadas.append(pessoas[cad])
        maPesadas.append(pessoas[cad])
    else:
        if pessoas[cad][1] > maPesadas[0][1]:
           maPesadas.clear()
           maPesadas.append(pessoas[cad])
        elif pessoas[cad][1] < mePesadas[0][1]:
           mePesadas.clear()
           mePesadas.append(pessoas[cad])
        elif maPesadas[0][1]==pessoas[cad][1]:
            maPesadas.append(pessoas[cad])
        elif mePesadas[0][1]==pessoas[cad][1]:
            mePesadas.append(pessoas[cad])
        
    cad+=1
    continuar = str(input('Continuar?[S/N] '))
    if continuar in 'nN':
        break
print(f'Pessoas {pessoas}\nMenor peso {mePesadas}\nMaior peso {maPesadas}')