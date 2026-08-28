print('------- DESAFIO 30 ---------')
# Crie um programa que leia um número inteiro na tela, e mostre se ele é PAR ou ÍMPAR.

from time import sleep
sleep(1.0)

print('------ PAR OU ÍMPAR -------')
num = int(input('Escolha um número inteiro: '))

if (num % 2 == 0):
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
