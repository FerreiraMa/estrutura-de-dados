import numpy as np


'''
O início da fila fica do lado direito
'''


class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0  # utilizada para verificar se o array encontra-se cheio e para fazer a inversão de lado.
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila esta cheia")
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila esta vazia")
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

fila = FilaCircular(5)
fila.primeiro()
print("####################################")

# 1
fila.enfileirar(1)
print(fila.primeiro())
print("####################################")

# 5 4 3 2 1
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
print("####################################")

# 'Fila esta cheia
fila.enfileirar(6)
print("####################################")

# 5 4 3
fila.desenfileirar()
fila.desenfileirar()
print(fila.primeiro())
print("####################################")

print(fila.valores) # Recomenda-se deixar com privado a variável valores
print("####################################")

# 7 6 5 4 3
fila.enfileirar(6)
fila.enfileirar(7)
print(fila.valores)
print(f'{fila.inicio} - {fila.valores[fila.inicio]}, {fila.final} - {fila.valores[fila.final]}')
