import NodeTree


class Arvore:

    def __init__(self, value=None):
        if value:
            self.raiz = NodeTree(value)
        else:
            self.raiz = None

    def calcula(self, node = None):
        if node is None:
            node = self.raiz
        if node.esq:
            calcula()
        print(node)
        if node.dir:
            node.calcula()
