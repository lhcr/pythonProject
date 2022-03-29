#Filas com listas
fila = []
fila.append('A')
fila.append('B')
fila.append('C')
print(fila)
fila.pop(0)
print(fila)
fila.pop(0)
print(fila)
fila.pop(0)
print(fila)

#Filas criando

from sre_constants import ANY
from typing import Any
# import Node


EMPTY_NODE_VALUE ='__EMPTY_NODE_VALUE__'
EMPTY_FILA_VALUE ='__EMPTY_FILA_VALUE__'

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node

    def __repr__(self) -> str:
        return f'{self.value}'

    def __bool_(self) ->bool:
        return bool(self.value!= EMPTY_NODE_VALUE)

class Fila:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0

    def push(self, value: Any) -> None:
        new_node = Node(value)

        if not self.first:
            self.first = new_node
        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self._count+=1


    def pop(self)-> Node:
        if not self.first:
            print('Erro')
        temp = self.first
        if not self.first.next:
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)
        self._count-=1
        return temp
    
    def peek(self)-> Node:
        return self.first

    def __len__(self)->int:
        return self._count

    def __bool__(self)->bool:
        if not self.first:
            return True
        else: 
            return False
    
    # def __iter__(self) -> Fila:
        # return self
    
    # def __next__(self) -> Any:
        