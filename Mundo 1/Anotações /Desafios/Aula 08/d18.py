print('---- DESAFIO 18 ------')
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

import math 
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cos:.2f}') 
print(f'Tangente: {tan:.2f}')
