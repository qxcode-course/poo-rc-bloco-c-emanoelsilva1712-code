class Pessoa:
    def __init__(self):
        self.idades = []

    def __init__(self):
        idades = [10, 20, 30, 40, 50]
        tamanho = len(idades)
        print(tamanho)

    def __str__(self):
        return f"idades: {self.idades}"

    def add_idade(self, idades: int):
        self.idades.append(5, idades)
    
    def remv_idade(self, idades: int):
        self.idades.pop(5, idades)

    def add_idades_inicio(self, idades: int):
        self.idades.insert(0, idades)

    def remv_idades_final(self, idades: int):
        self.idades.pop(0, idades)

    def add_idades_especifica(self, idades: int):
        self.idades.insert(3, idades)

    def remv_idades_especifica(self, idades: int):
        self.idades.pop(3, idades)

def main():
    pessoa = Pessoa()
    while True:
        line = input()
        args = line.split()

        cmd = args[0]

        if cmd == "init":
            passoa = Pessoa()

        elif cmd == "show":
            print(pessoa)

        elif cmd == "adicionar idades":
            pessoa.add_idade(int(args[1]))
    
        elif cmd == "remover idades":
            pessoa.remv_idade(int(args[1]))

        elif cmd == "adicionar idades inicio":
            pessoa.add_idades_inicio(int(args[1]))

        elif cmd == "remover idades inicio":
            pessoa.remv_idades_final(int(args[1]))

        elif cmd == "adicionar idades especifico":
            pessoa.add_idades_especifica(int(args[1]))

        elif cmd == "remover idades especifico":
            pessoa.remv_idades_especifica(int(args[1]))

        