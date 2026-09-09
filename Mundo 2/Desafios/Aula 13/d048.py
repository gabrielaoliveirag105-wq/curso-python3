print('----- DESAFIO 48 ------')
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

verde = '\033[4;32m'
limpa = '\033[m'

print(f'{verde}--- MÚLTIPLOS DE TRÊS ---{limpa}')

total = 0
soma = 0

for c in range (3, 500+1,3):
    if c % 2 == 1:
        soma = soma + c
        total = total + 1 # quantos números são múltiplos 
        print(c)

print(f'\nAo todo são {verde}{total}{limpa} números múltiplos por três \nA soma de todos os números múltiplos por 3 é: {verde}{soma}{limpa}')