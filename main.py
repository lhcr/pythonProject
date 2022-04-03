import Arvore
import NodeTree
# import pythonRecursao
# import Fila
# import Pilha
# import listaEncadeada



a = Arvore.Arvore()
n1 = NodeTree.NodeTree('a')
n2 = NodeTree.NodeTree('+')
n3 = NodeTree.NodeTree('*')
n4 = NodeTree.NodeTree('b')
n5 = NodeTree.NodeTree('-')
n6 = NodeTree.NodeTree('/')
n7 = NodeTree.NodeTree('c')
n8 = NodeTree.NodeTree('d')
n9 = NodeTree.NodeTree('e')

n6.esq = n7
n6.dir = n8
n5.esq = n6
n5.dir = n9
n3.esq = n4
n3.dir = n5
n2.esq = n1
n2.dir = n3
a.raiz = n2

a.calcula()
# print(a.raiz.esq.valeu)
# print(a.raiz.dir.valeu)




# print(pythonRecursao.fatorial(5))



# lista = listaEncadeada.ListaEncadeada()

# lista.insere(10,0)
# lista.insere(6,1)
# lista.insere(9,2)
# lista.insereFim(8)
# lista.__setitem__(1,8)

# print(f'{lista.remove(2)}')

# print(f'{lista.__repr__()}')

#n1=int(input('digite um número '))
#n2=int(input('digite mais um número '))
#s=n1+n2
#print('soma {}', format((n1+n2),int))
#print('a soma entre {} e {} vale {}'.format(n1,n2,s))

# pilha = Pilha.Pilha()

# pilha.push(6)
# pilha.push(9)
# pilha.push(10)
# pilha.push(14)


# print(f'{pilha.__repr__()}')

# fila = Fila.Fila()

# fila.insere(4)
# fila.insere(1)
# fila.insere(9)

# print(f'{fila.__repr__()}')

# fila.remove()

# print(f'{fila.__repr__()}')
