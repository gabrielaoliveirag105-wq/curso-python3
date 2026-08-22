print('---------- DESAFIO 27 ----------')
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

''' Exemplo:
nome = Ana Maria Da Silva
primeiro = Ana
último = Souza'''

nome = str(input('Digite seu nome completo: '))

primeiro = (nome.split()[0])
ultimo = (nome.split()[-1])

print(f'Primeiro: {primeiro}')
print(f'Último: {ultimo}')
