

class NodeTree:
    def __init__(self,value) -> None:
        self.value = value
        self.esq = None
        self.dir = None

    def __str__(self) -> str:
        return str(self.value)
