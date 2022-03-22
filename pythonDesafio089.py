dados = []
alunos = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    alunos.append((dados[1]+dados[2])/2)
    dados.clear()
    continuar = str(input('Continuar?[S/N] '))
    if continuar in 'nN':
        break
print(alunos)