print('----- DESAFIO 48 ------')
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

verde = '\033[4;32m'
limpa = '\033[m'

print(f'{verde}--- MÚLTIPLOS DE TRÊS ---{limpa}')

soma = 0
for c in range (1, 500+1):
    if c % 3 == 0:
        soma = soma + c
        print(c)

print(f'\nA soma de todos os números múltiplos por 3 é: {verde}{soma}{limpa}')