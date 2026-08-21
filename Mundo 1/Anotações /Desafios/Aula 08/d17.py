print('---- DESAFIO 17 ------')
# Faça um programa que leia   o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
oposto = float(input('Cateto Oposto: '))
adjacente = float(input('Cateto Adjacente: '))
hipo = math.hypot(oposto,adjacente)

print(f'A hipotenusa é: {hipo:.2f}')

