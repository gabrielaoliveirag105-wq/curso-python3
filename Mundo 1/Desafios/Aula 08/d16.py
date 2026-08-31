print('---- DESAFIO 16 ------')
# Faça um programa que leia um número real qualquer e mostre na tela sua porção inteira.

import math 
num = float(input('Digite um número real qualquer: '))
inteira = math.trunc(num)
print(f'A parte inteira de {num} é {inteira}.')

# Feito com biblioteca, mas é possível com operação arit. divisão p/ inteira (//) 