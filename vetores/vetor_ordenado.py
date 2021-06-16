import numpy as np


'''
Vantagem: Pesquisa de dados leva menos tempo
Desvantagem: Inserção de dados leva mais tempo

Pesquisa binária é O(log n) é mais eficiente, mas a lista de dados deve estar ordenada
'''

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor esta vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    #O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1

    # O(log n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_superior + limite_inferior)/2)
            # Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se não achou
            elif limite_inferior > limite_superior:
                return - 1
            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                # Limite superior
                else:
                    limite_superior = posicao_atual - 1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

vetor = VetorOrdenado(5)
vetor.imprime()
print("####################################")

vetor.insere(6)
vetor.imprime()
print("####################################")

vetor.insere(1)
vetor.imprime()
print("####################################")

vetor.insere(8)
vetor.imprime()
print("####################################")

vetor.insere(4)
vetor.imprime()
print("####################################")

vetor.insere(2)
vetor.imprime()
print("####################################")

print(f'Posição: {vetor.pesquisar(8)}')
print("####################################")

vetor.excluir(6)
vetor.imprime()
print("####################################")

print(vetor.pesquisa_binaria(4))
