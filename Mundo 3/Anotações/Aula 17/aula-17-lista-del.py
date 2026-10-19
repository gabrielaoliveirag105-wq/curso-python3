# Aula 17 - Deletando elementos de uma lista

lanche = ['suco', 'pizza', 'picolé', 'hamburguer'] # aqui criamos uma lista que vai até hamburguer com 4 elementos

lanche.append('cookie') # adicionamos o elemento cookie ao final da lista, sem a necessidade de criar uma nova lista ou modificar a lista original.

lanche.insert(0, 'cachorro-quente') # aqui adiionamos o novo elemento no início da lista, na posição 0, antes do elemento que já estava lá.

del lanche[0] # O del remove o elemento da lista, aqui elimina o elemento 0 que foi adicionado anteriormente.

lanche.pop()# geralmente é usado para eliminar o último item, mas pode ser usado para outros elementos.

lanche.remove('suco') # com o remove indicamos o valor que você quer remover.

print(lanche)