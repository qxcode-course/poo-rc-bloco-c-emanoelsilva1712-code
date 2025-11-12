class Cliente: 
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.__nome}"

class Mercantil:
    def __init__(self, n_caixas: int):
        self.caixas: list[Cliente | None] = []
        self.fila: list[Cliente] = []
        
        for _ in range (n_caixas):
            self.caixas.append(None) 

    def __str__(self): 
        caixas = ", ".join([str(x) if x else "-----" for x in self.caixas])
        fila = ", ".join([str(x) for x in self.fila])
        return f"Caixas: [{caixas}]\nEspera: [{fila}]"
    
    def map(self, lista: list):
        ls: list = []
        for elemento in lista:
            if elemento is None:
                ls.append("-----")
            else:
                ls.append(str(elemento))
        return ls
        # variavel = map (caixas)
        # variavel = map (fila)


    def chegar(self, Cliente: Cliente):
        self.fila.append(Cliente)

    def chamar(self, index: int):

        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return

        elif len(self.fila) == 0:
            print("fail: fila vazia")
            return

        elif self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return

        self.caixas[index] = self.fila.pop(0)    #pop = retorno o primeiro cliente da fila e retorna ele

    def finish(self, index: int) -> Cliente | None:

        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return None

        elif self.caixas[index] is None:
            print("fail: caixa vazio")
            return None
            
        aux = self.caixas[index]

        self.caixas[index] = None
        return aux
        
def main():
    mercantil: Mercantil | None = None
    
    while True:
        try:
            line = input()
            args = line.split()

            if not args:
                continue
            
            print("$" + line)
            cmd = args[0]

            if cmd == "init":
                mercantil = Mercantil(int(args[1]))

            elif cmd == "show":
                print(mercantil)

            elif cmd == "arrive":
                mercantil.chegar(Cliente(args[1]))
            
            elif cmd == "call":
                mercantil.chamar(int(args[1]))

            elif cmd == "finish":
                mercantil.finish(int(args[1]))
                
        except EOFError:

            break

main()