from collections import Counter
from itertools import cycle
from time import perf_counter_ns

lista_de_numeros = list(range(10))
print(id(lista_de_numeros))
print(id(lista_de_numeros[0]))
print(id(lista_de_numeros[1]))
print(id(lista_de_numeros[2]))

'''
140519288280576 = endereço de memória da lista
140519289702672 = endereço do elemento 0 = 140519289702672 + posição 0 * 32
140519289702704 = endereço do elemento 1 = 140519289702672 + posição 1 * 32
140519289702736 = endereço do elemento 2 = 140519289702672 + posição 2 * 32

a diferença entre os endereços dos elemento é de 32 bits
'''

maior_delta = 0
counter = Counter()
with open('/home/brferreiram/arq.txt', 'w') as arquivo:
    for i in cycle([11, 12]):
        id_final = id(lista_de_numeros)
        inicio = perf_counter_ns()
        lista_de_numeros.append(i)
        delta = perf_counter_ns() - inicio
        counter[delta] += 1
        arquivo.write(f'{counter} \n')
    #print(counter)
