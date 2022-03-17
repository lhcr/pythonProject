dados = list()
dados.append('Pedro')
dados.append(25)
pessoas = []
pessoas = [['Pedro',25],['Maria', 20],['Joao',30]]
pessoas.append(dados[:])#copia de dados, cadastro de uma lista dentro de outra
# class pessoas:
    # nome = ''
    # idade = 
aliens = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    aliens.append(dado[:])
    dado.clear()#limpa toda lista

for p in aliens:#percorre a estrutura aliens
    if p[1]>=21:
        print(p[0])