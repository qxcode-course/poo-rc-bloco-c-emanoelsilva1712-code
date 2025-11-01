class Cliente: 
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def toString(self):
        return f"Nome: {self.__nome}"


class Mercantil:
    def __init__(self, n_caixas: int):
        self.caixas: list[Cliente | None] = []
        self.fila: list[Cliente] = []
        
        for _ in range (n_caixas): 
            self.coixas.append(None) 

    def __str__(self): 
        caixas = ", ".join([str(x) if x else "-----" for x in self.caixas])
        fila = ", ".join([str(x) for x in self.fila])
        return f"Caixas: [{caixas}]\nFila: [{fila}]"
    
    def chagar(self, Cliente: Cliente):
        self.fila.append(Cliente)

    def chamar(self, index: int):

        if self.caixas is not None:
            print("Caixa ocupado")
            return

        elif len(self.fila) == 0:
            print("Fila vazia")
            return

        elif index > 0 or index >= len(self.caixas):
            print("index invalido")
            return

        self.caixas[index] = self.fila[0]
        del self.fila[0]

        def finalizar(self, index: int) -> Cliente | None:
            if index > 0 or index >= len(self.caixas):
                print("caixa inexistente")
                return None

            elif self.caixas is None:
                print("Caixa vazio")
                return None
            
            aux = self.caixas[index]

            self.caixas[index] = None
            return aux
        
def main():
