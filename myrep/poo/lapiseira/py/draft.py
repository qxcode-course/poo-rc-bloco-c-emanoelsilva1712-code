class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        #Retorna o desgaste do grafite por folha de acordo com a dureza.
        desgaste = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return desgaste.get(self.hardness, 1)

    def __str__(self) -> str:
        return f"[{self.thickness}:{self.hardness}:{self.size}]"


class Lapiseira:
    def __init__(self, thickness: float = 0.0):
        self.thickness: float = thickness
        self.bico: Lead | None = None
        self.tambor: list[Lead] = []   #grafite no tambor

    #ver se é compativel
    def insert(self, lead: Lead):
        if abs(lead.thickness - self.thickness) > 1e-6:
            print("fail: calibre incompativel")
            return
        self.tambor.append(lead)   #Adiciona grafite no final

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        
        if not self.tambor:     #ola se o tambor esta vazio
            print("fail: nao existe grafite no tambor")
            return
        
        self.bico = self.tambor.pop(0)  #Remove o primeiro grafite do tambor e coloca no bico

    def remove(self):

        if self.bico is None:
            print("fail: nao existe bico")
            return
        
        self.bico = None #Remove o grafite do bico

    def writePage(self):

        if self.bico is None:
            print("fail: nao existe no bico")
            return
        
        if self.bico.size <= 10:
            print("fail: tamanho insuficiente")
            self.bico = None   #retira o grafite unutiu
            return
        
        desgaste = self.bico.usagePerSheet()

        if self.bico.size - desgaste < 10:
            self.bico.size = 10
            print("fail: folha incompleta")
            self.bico = 10     #maximo do grafite
            return
        
        self.bico.size -= desgaste  #desgasta o grafite

    def __str__(self):

        grafite_bico_str = str(self.bico) if self.bico else "[]"
        grafites_tambor_str_list = [str(g) for g in self.tambor]

        if not grafites_tambor_str_list:
            grafites_tambor_str = "<>"
        else:
            grafites_tambor_str = "<" + ", ".join(grafites_tambor_str_list) + ">"

        return f"calibre: {self.thickness}, bico: {grafite_bico_str}, tambor: {grafites_tambor_str}"


def main():
    lapiseira = Lapiseira()

    while True:

        line = input()
        print("$" + line)
        args = line.split()

        if not args:
            continue

        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "init":
            lapiseira = Lapiseira (float(args[1]))
        elif cmd == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            lead = Lead(thickness, hardness, size)
            lapiseira.insert(lead)
        elif cmd == "pull":  #puxa um grafite do tambor para o bico
            lapiseira.pull()
        elif cmd == "remove":
            lapiseira.remove()
        elif cmd == "write":
            lapiseira.writePage()
        elif cmd == "show":
            print(lapiseira)
        else:
            print("fail: comando invalido")


main()
