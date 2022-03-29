#import Node

from ctypes import pointer
from platform import node


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self,value):
            temp = Node(value)
            temp.next =self.top
            self.top = temp
            self._size+=1

    def pop(self):
        if self._size>0:
            temp = self.top
            self.top = self.top.next
            self._size -= 1
            return temp
        else:
            raise IndexError("Erro")

    def getTop(self):
        if self._size>0:
            return self.top.value
        else:
            raise IndexError("Erro")


    def __len__(self):
        return self._size
    
    def __repr__(self):#representação da lista
        temp =""
        pointer = self.top
        while(pointer):
            temp = temp +str(pointer.value)+"\n"
            pointer =pointer.next
        return temp

    def __str__(self):
        return self.__repr__()