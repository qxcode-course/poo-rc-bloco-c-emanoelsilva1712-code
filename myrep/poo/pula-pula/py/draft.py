class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = int(idade)

    def __str__(self):
        return f"{self.nome}:{self.idade}"
    
class Pula:
    def __init__(self):
        self.fila: list[Pessoa] = []
        self.dentro: list[Pessoa] = []

    def arrive(self, pessoa):
        self.fila.insert(0, pessoa)

    def enter(self):
        if self.fila:
            criança = self.fila.pop(0)
            self.dentro.append(criança)

    def leave(self):
        if self.dentro:
            criança = self.dentro.pop(0)
            self.fila.append(criança)

    def remove(self, nome):     #remove da fila
        for i, p in enumerate(self.fila):
            if p.nome == nome:
                self.fila.pop(i)
                return
            
        for i, p in enumerate(self.dentro):   #remove do pula pula
            if p.nome == nome:
                self.dentro.pop(i)
                return
            
    def __str__(self):
        fila = "[" + ", ".join(str(p) for p in self.fila) + "]"
        dentro = "[" + ", ".join(str(p) for p in self.dentro) + "]"
        return f"{fila} => {dentro}"

def main():
    pula = Pula()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "arrive":
            pula.arrive(Pessoa(args[1], args[2]))

        elif args[0] == "enter":
            pula.enter()

        elif args[0] == "leave":
            pula.leave()

        elif args[0] == "show":
            print(pula)

        elif args[0] == "remove":
            pula.remove(args[1])

        