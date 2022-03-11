# Listas
from audioop import reverse


comida = ['Hambúrguer','cerveja','batata frita']
print(comida)
comida.append('açaí') #adiciona no fim da lista
print(comida)
comida.insert(2,'banco') #adiciona em qualquer parte da lista
print(comida)
del comida[2] #elimina elemento da posição informada
print(comida) 
comida.pop(2) #mais usado para eliminar do fim da lista, mas serve para eliminar em qualquer parte
print(comida)
comida.remove('açaí') #remove pela informação e não pelo índice
print(comida)
comida.pop()#remove o último elemento
print(comida)

valor = list(range(4,11))#cria uma lista de 4 até 10
valor.sort()#ordena valores
valor.sort(reverse=True)#inverte a ordem da lista
print(valor)
for c,v in enumerate(valor):
    print(f'{v}...{c}', end='')

valor = comida #ligação entre lista
print(f'{valor}\n{comida}')
valor = comida[:] #cópia de comida dentro de valor