print('---- DESAFIO 19 ------')
# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'O nome sorteado para apagar o quadro é: {escolhido}')