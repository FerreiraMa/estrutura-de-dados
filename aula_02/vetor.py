from array import array


'''
h = signed short int = 2 bytes = 16 bits 
16 bits -1 bits do sinal   = 2**15 -1(porque começa do zero) = 32767

Array não é muito utilizado!
'''
vetor = array('h', [1, 2, 3, 4, 5])

print(type(vetor))
print(vetor)
print(vetor[0], vetor[-1])
vetor.append(6)
print(vetor[0], vetor[-1])
print(vetor)
