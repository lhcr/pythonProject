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
