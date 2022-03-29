import Fila
import Pilha
import listaEncadeada
import Filas



fila = Filas.Fila()
lista = listaEncadeada.ListaEncadeada()

lista.insere(10)
lista.insere(6)
lista.insere(9)
lista.__setitem__(1,8)
temp = lista.head
for i in range(0,lista.__len__()):
    print(temp.value)
    temp = temp.next


#n1=int(input('digite um número '))
#n2=int(input('digite mais um número '))
#s=n1+n2
#print('soma {}', format((n1+n2),int))
#print('a soma entre {} e {} vale {}'.format(n1,n2,s))

pilha = Pilha.Pilha()

pilha.push(6)
pilha.push(9)
pilha.push(10)
pilha.push(14)


print(f'{pilha.__repr__()}')

fila = Fila.Fila()

fila.insere(4)
fila.insere(1)
fila.insere(9)

print(f'{fila.__repr__()}')

fila.remove()

print(f'{fila.__repr__()}')
