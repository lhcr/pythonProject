dados = {}
alunos = []
while True:
    dados['nome'] = str(input('Nome: '))
    dados['media'] =float(input('Média: '))
    if dados['media']>=7:
        dados['situacao'] = 'Aprovado'
    else:
        dados['situacao'] = 'Reprovado'
    alunos.append(dados.copy())        
    dados.clear()
    continuar = str(input('Continuar?[S/N] '))
    if continuar in 'nN':
        break
print(alunos)

