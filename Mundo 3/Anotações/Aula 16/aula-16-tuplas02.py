# Aula 16 - Teste Tuplas

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#for c in range (0, len(lanche)):
#   print(f'Eu vou comer {lanche[c]} na posição {c}')# Mostra a posição de cada elemento na tupla

#for comida in lanche:
#   print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') # Mostra a posição de cada elemento na tupla

