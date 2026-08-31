print('---------- DESAFIO 27 ----------')
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

''' Exemplo:
nome = Ana Maria Da Silva
primeiro = Ana
último = Souza'''

nome = str(input('Digite seu nome completo: ')).strip()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {nome[0]}')
print(f'E o último é: {nome[-1]}')
