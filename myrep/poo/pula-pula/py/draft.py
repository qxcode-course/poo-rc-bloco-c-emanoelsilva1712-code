class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getAge(self):
        return self.__idade
    
    def getNome(self):
        return self.__nome

    def setAge(self, age: int):
        self.__idade = age

    def setNome(self, nome: str):
        self.__nome = nome

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
    
class Pula:
    def __init__(self):
        self.__fila: list[Pessoa] = []
        self.__dentro: list[Pessoa] = []

    def arrive(self, nome: str, age: int):
        pessoa = Pessoa(nome, age)
        self.__fila.insert(0, pessoa)

    def enter(self):
        if not self.__fila:
            print(f"fila vazia")
        self.__dentro.insert(0, self.__fila[len(self.__fila)-1])
        self.__fila.pop(len(self.__fila)-1)

    def leave(self):
        if not self.__dentro:
            return
        
        self.__fila.insert(0, self.__dentro[len(self.__dentro)-1])
        self.__dentro.pop(len(self.__dentro)-1)

    def remove(self, nome: str):     #remove da fila
        for i, pessoa in enumerate(self.__fila):
            if pessoa.getNome() == nome:
                self.__fila.pop(i)
                return
            
        for i, pessoa in enumerate(self.__dentro):   #remove do pula pula
            if pessoa.getNome() == nome:
                self.__dentro.pop(i)
                return
            
        print(f"fail: {nome} nao esta no pula-pula")

    def __str__(self):
        fila_str = "[" + ", ".join(str(p) for p in self.__fila) + "]"
        dentro_str = "[" + ", ".join(str(p) for p in self.__dentro) + "]"
        return f"{fila_str} => {dentro_str}"

def main():
    pula = Pula()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(pula)

        elif args[0] == "arrive":
            pula.arrive(args[1], int(args[2]))

        elif args[0] == "enter":
            pula.enter()

        elif args[0] == "leave":
            pula.leave()

        elif args[0] == "remove":
            pula.remove(args[1])
        else:
            return "fail: comando invalido"

main()
        