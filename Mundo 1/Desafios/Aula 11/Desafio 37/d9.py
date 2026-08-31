print('------ DESAFIO 37 ------')
# Pegue alguns desafios e coloque um sistema de cores.

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'O nome sorteado para apagar o quadro é: \033[4;36m{escolhido}\033[m')