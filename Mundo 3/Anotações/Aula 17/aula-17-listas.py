# Aula 17 - Listas (Parte 1)
# Usamos [ ] para criar listas em Python, e diferente das Tuplas, as listas são mutáveis, ou seja, podemos alterar seus elementos. 
# append() - Adiciona um elemento ao final da lista. 

lanche = ['suco', 'pizza', 'picolé', 'hamburguer'] # aqui criamos uma lista que vai até hamburguer com 4 elementos

lanche.append('cookie') # adicionamos o elemento cookie ao final da lista, sem a necessidade de criar uma nova lista ou modificar a lista original.

lanche.insert(0, 'cachorro-quente') # aqui adiionamos o novo elemento no início da lista, na posição 0, antes do elemento que já estava lá.

print(lanche)
