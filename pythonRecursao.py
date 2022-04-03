from collections import namedtuple
from typing import List



def fatorial(n: int)-> int:
    if n==0:
        return 1
    n*=fatorial(n-1)
    return n


box = namedtuple('box', 'have_key')

boxs: List[box] = [
    box(False), box(
        False), box(False),
    box(True),  box(
        False), box(False),
    box(False), box(False), box(False)]


def encotraChave(boxs: List[box], index: int =0):
    if len(boxs)<=index:
        return box(False)
    box = boxs[index]

    if box.have_key:
        return box
    
    index+=1
    return encotraChave(boxs,index)


print(encotraChave(boxs))





