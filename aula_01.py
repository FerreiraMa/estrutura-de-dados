from math import inf
from time import time

"""
Estudos Experimentais - Desafio:

Processos Disputando CPU
Dificuldade de comparar dois algoritmos
Limitação de Entradas no programa
Necessidade de implementar o algoritmo

Tamanho da Entrada
Função f(n)
Utilizada para o pior caso
Contar o número de funções primitivas
Funções primitivas corresponde a instruções de nível-baixo com execução em tempo constante.

Funções:
Constant = 1 (Busca de um elemento em uma lista quando se conhece o seu índice)
Logarithm = logn
Linear = n
n-log-n = nlogn (AAlgoritmo de ordenação)
quadratic = n²
Cubic = n³
Exponential= a^n 

Big - Oh = O(n)

"""

def meu_max(iteravel):
    """
    Análise do algoritmo
    Em tempo de execução, algoritmo O(N)
    Em memória O(1)
    :param iteravel:
    :return:
    """
    numero_maximo = -inf
    for numero in iteravel:
        if numero > numero_maximo:
            numero_maximo = numero
    return numero_maximo


if __name__ == '__main__':
    print(meu_max([1]))
    print(meu_max([1, 100]))
    print('Estudo Experimentação sobre o tempo de execução da função max')
    inicio = 1_000_000
    for n in range(0, inicio * 20 + 1, inicio):
        inicio = time()
        meu_max(range(n))
        fim = time()
        tempo_de_execucao_em_segundos = fim - inicio
        print('*' * int(tempo_de_execucao_em_segundos * 10), n)
