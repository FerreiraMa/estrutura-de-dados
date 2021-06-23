import numpy as np


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)  # Novo recebe o endereço de memória onde a estrutura da class No encontra-se armazenada
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def pesquisar(self, valor):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
        return atual

    # A função não exclui o valor, apenas aponta para o próximo
    # O SO irá excluir fazendo a 'limpeza'
    def excluir_inicio(self):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print('A lista está vazia!')
            return None

        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual

lista = ListaEncadeada()
lista.insere_inicio(1)
lista.mostrar()
print(lista.primeiro)  # Mostra o endereço de memória
print("####################################")

# 2, 1 - Insere na frente
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()
print(lista.primeiro.proximo.proximo.proximo.proximo) # Mostra o endereço do número 1
print("####################################")

lista.excluir_inicio()
lista.excluir_inicio()
print(lista.mostrar())
print("####################################")

print(lista.pesquisar(3).valor)
print("####################################")

print(lista.excluir_posicao(1))
print(lista.mostrar())
print("####################################")