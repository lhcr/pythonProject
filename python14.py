#dicionários
dados = dict()
dados2 = {}
dados3 = {'nome':'Luis','idade':'35'}#indices são 'nome' e 'idade'
dados3['sexo']='M'#adiciona novo campo e novo dado
del dados3['idade']#elimina o campo idade
print(dados3.values())#metodo que retorna os valores 
print(dados3.keys())#metodo que retorna os indices
print(dados3.items())#meto*do que retorna os indices e valores
for k,v in dados3.items():
    print(k,v)

pessoas = {'nome':'Luis','idade':'35'}
print(f'{pessoas["nome"]}')

brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1.copy())#metodo copy copia dicionario sem vinculação
brasil.append(estado2.copy())

