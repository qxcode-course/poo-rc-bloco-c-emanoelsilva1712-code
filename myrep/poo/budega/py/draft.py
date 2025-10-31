class Cliente: 
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def toString(self):
        return f"Nome: {self.__nome}"


class Mercantil:
    def __init__(self, caixas: int):
        self.coixas = None
        self.fila: int = 0

    def toString(self):
        

    