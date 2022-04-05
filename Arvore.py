from platform import node
import NodeTree


class Arvore:

    def __init__(self, value=None):
        if value:
            node = NodeTree.NodeTree(value)
            self.raiz = node
        else:
            self.raiz = None


    def calcula(self, node=None):
        if node is None:
            node = self.raiz
        if node.esq:
            print('(', end='')
            self.calcula(node.esq)
        print(f'{node}', end='')
        if node.dir:
            self.calcula(node.dir)
        print(')', end='')


    def altura(self, node=None):
        if node is None:
            node = self.raiz
        aEsq = 0
        aDir = 0
        if node.esq:
            aEsq = self.altura(node.esq)
        if node.dir:
            aDir = self.altura(node.dir)
        if aEsq > aDir:
            return aEsq + 1
        return aDir + 1
