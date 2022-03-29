

from ctypes import pointer


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._size = 0


    def insere(self, value):
        temp = Node(value)
        if self.fim is None:
            self.fim = temp
            self.inicio = self.fim            
        else:
            self.fim.next = temp
            self.fim = temp
        self._size += 1



    def remove(self):
        if self.inicio:
            temp = self.inicio
            self.inicio = self.inicio.next
            self._size-=1
        return temp
    
    def __len__(self):
        return self._size

    def __repr__(self):
        ponteiro = self.inicio
        temp = ''
        while ponteiro:
            temp = temp +str(ponteiro.value) +' // ' 
            ponteiro = ponteiro.next
        return temp

    def __str__(self):
        return self.__repr__()

    