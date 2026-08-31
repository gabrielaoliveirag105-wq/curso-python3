print('---- DESAFIO 20 ------')  
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e a ordem sorteada.

from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
ordem = shuffle(lista)

print(f'A ordem para apresentar o trabalho é: \n{lista}')