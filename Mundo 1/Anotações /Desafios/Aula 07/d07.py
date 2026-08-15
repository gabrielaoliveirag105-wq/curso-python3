print('------ DESAFIO 07 ------') 
# Faça um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nome = input('Nome do (a) aluno (a): ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media  = (n1 + n2) / 2 # Calcula primeiro a nota, e depois divide.
print(f'O (a) aluno (a) {nome}, ficou com média final de {media:.1f}') 