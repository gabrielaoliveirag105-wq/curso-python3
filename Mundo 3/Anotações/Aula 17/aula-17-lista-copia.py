# Aula 17 - Copiando e alterando lista

a = [2,3,4,7]
b = a[:] # Altera somente o valor da lista B
b[2] = 8 # Esse elemento vai para lista B sem mudar sua raiz que é a lista A
print(f'Lista A: {a}')
print(f'Lista B: {b}')