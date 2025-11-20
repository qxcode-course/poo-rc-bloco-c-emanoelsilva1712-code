import random

class Pessoa:
    def __init__(self):
        self.idades = [10, 20, 30, 40, 50]
        print(f"Lista Inicial: {self.idades}")

    def __str__(self):
        return f"idades: [{", ".join(map(str, self.idades))}] | Tamanho: {len(self.idades)}"

    def add_idade(self, idades: int):
        self.idades.append(idades)

    def remv_idade(self):
        if self.idades:
            return self.idades.pop()
        return None

    def add_idades_inicio(self, idades: int):
        self.idades.insert(0, idades)

    def remv_idades_inicio(self):
        if self.idades:
            return self.idades.pop(0)
        return None

    def add_idades_especifica(self, indece: int, idades: int):
        self.idades.insert(indece, idades)

    def remv_idades_especifica(self, indece: int):
        if 0 <= indece < len(self.idades):
            return self.idades.pop(indece)
        return None

    def sequencia(self, n: int) -> list[int]:
        return list(range(n))
        
    def valores_aleatorios(self, n: int) -> list[int]:
        return [random.randint(1, 100) for _ in range(n)]

    def procurar_idades(self, idades: int) -> int:
        try:
            return self.idades.index(idades)
        except ValueError:
            return -1
        

pessoa = Pessoa()
    
pessoa.add_idade(60)
print(f"Add final (60): {pessoa}")
removido_final = pessoa.remv_idade()
print(f"2. Rem final ({removido_final}): {pessoa}")

pessoa.add_idades_inicio(0)
print(f"3. Add inicio (0): {pessoa}")
removido_inicio = pessoa.remv_idades_inicio()
print(f"4. Rem inicio ({removido_inicio}): {pessoa}")

pessoa.add_idades_especifica(2, 25)
print(f"5. Add pos 2 (25): {pessoa}")
removido_pos = pessoa.remv_idades_especifica(2)
print(f"6. Rem pos 2 ({removido_pos}): {pessoa}")

sequencia_nova = pessoa.sequencia(5)
print(f"7. Sequencia (0 a 4): {sequencia_nova}")
aleatoria_nova = pessoa.valores_aleatorios(5)
print(f"8. Aleatoria (5 vals): {aleatoria_nova}")

indece = pessoa.procurar_idades(40)
print(f"9. Busca 40 (index): {indece}")
