# Aula 16 - Tuplas 
# Tuplas/ Variáveis compostas, podem armazenar vários valores, e são imútaveis, ou seja, não podem ser alteradas depois de criadas.

lanche  = 'Hamburguer', 'Pizza', 'Refri', 'Sorvete'
print(lanche[2]) #Mostra o elemento na posição 2
print(lanche[0:2])#Mostra os elementos da posição 0 até a posição 2.
print(lanche[-0]) #Mostra o último elemento

# Lendo Tuplas

lanche = 'Hamburguer', 'Pizza', 'Suco', 'Sorvete'
print(len(lanche)) #Mostra a quantidade de elementos na tupla

c = " "
for c in lanche:
    print(c)