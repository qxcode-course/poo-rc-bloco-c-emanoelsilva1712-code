class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getPhone(self):
        return self.__phone
    
    def setPhone(self, fone: int):
        self.__phone = fone

    def getId(self):
        return self.__id
    
    def setId(self, id: str):
        self.__id = id

    def __str__(self):
        return f"{self.__id}:{self.__phone}"

class Sala:
    def __init__(self, cap: int):
        self.__seats = [None] * cap    # seats = cadeiras 
        self.__search = [None] * cap     # search = procurar

    def _verifyIndex(self, index: int) -> bool:
        if 0 <= index < len(self.__seats):
            return True
        return False
        
    def _search(self, id: str) -> int:
        for i, client in enumerate(self.__seats):
            if client is not None and client.getId() == id:
                return i
        return -1

    def __str__(self):
        qtd = " ".join("-" if i is None else str(i) for i in self.__seats)
        return f"[{qtd}]"

    def reserve(self, id: str, phone: int, index: int):
        if not self._verifyIndex(index):
            print("fail: cadeira nao existe")
            return 
        
        elif self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return 
        
        elif self._search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return 
        
        client = Client(id, phone)
        self.__seats[index] = client
        return True

    def cancel(self, id: str):
        index = self._search(id)

        if index == -1:
            print("fail: cliente nao esta no cinema")
            return
        
        self.__seats[index] = None
        return

def main():
    sala = Sala(0)
    while True:

        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            sala = Sala(int(args[1]))

        elif args[0] == "show":
            print(sala)

        elif args[0] == "reserve":
            sala.reserve(args[1], int(args[2]), int(args[3]))
                        
        elif args[0] == "cancel":
            sala.cancel(args[1])

        else:
            print("fail: comando invalido")

main()