# Aula 16 - Tuplas

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche)) # Mostra os elementos da tupla em ordem alfabética, mas não altera a tupla original.'''

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c) # Mostra a junção das tuplas a e b, formando uma nova tupla c.
print(len(c)) # Mostra a quantidade de elementos na tupla c.
print(c.count(5)) # Mostra quantas vezes o elemento 5 aparece na tupla c.
print(c.index(8)) # posição em que está o elemento 8.