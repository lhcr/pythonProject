from platform import node
from typing import Any
import Node

class ListaEncadeada:

    def __init__(self):
        self.head = None
        self._size = 0

    def insere(self,value):
        if self.head:
            ultimo = self.head
            while(ultimo.next):
                ultimo = ultimo.next
            ultimo.next = Node.Node(value)
        else:
            self.head = Node.Node(value)
        self._size+=1

    def __len__(self)-> int:
        return self._size

    def __getitem__(self, index):
        if self.head:
            ultimo = self.head
            for i in range(index):
                ultimo = ultimo.next
            if ultimo:
                return ultimo
            raise IndexError("Erro")
        else:
            raise IndexError("Erro")

    def __setitem__(self, index, value):
        if self.head:
            ultimo = self.head
            for i in range(index):
                ultimo = ultimo.next
            if ultimo:
                ultimo.value = value
            else:
                raise IndexError("Erro")
        else:
            raise IndexError("Erro")


        
    
