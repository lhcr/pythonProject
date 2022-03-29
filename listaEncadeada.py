from typing import Any
import Node

class ListaEncadeada:

    def __init__(self):
        self.head = None
        self._size = 0

    def insere(self,value,indice):
        no = Node.Node(value)
        if indice == 0:
            no.next = self.head
            self.head = no
        else:
            proximo = self.head
            for i in range(indice-1):
                proximo = proximo.next
            no.next = proximo.next
            proximo.next = no
        self._size+=1

    def insereFim(self, value):
        no = Node.Node(value)
        proximo = self.head
        for i in range(self._size-1):
            proximo = proximo.next
        proximo.next = no
        self._size += 1

    def remove(self,indice):
        if self._size>=indice:
            proximo = self.head
            for i in range(indice):
                ant = proximo
                proximo = proximo.next
            temp = proximo.value
            ant.next = proximo.next
            self._size-=1
            return temp
        else:
            raise IndexError("Erro")
    


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
    
    def __repr__(self) -> str:
        temp = self.head
        imprime =''
        while temp:
            imprime = imprime + str(temp.value) + ' >> '
            temp = temp.next
        return imprime


        
    
