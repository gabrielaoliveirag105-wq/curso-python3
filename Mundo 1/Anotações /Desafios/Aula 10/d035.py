print('------- DESAFIO 35 ---------')
# Desenvolva um programa que leia o comprimento de três retas e diga aos usuário se elas podem ou não formar um triângulo.

from time import sleep
sleep(1.0)

print('----- CÁLCULO TRIÂNGULO ------')
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print(f'As retas {l1}, {l2} e {l3} PODEM FORMAR um TRIÂNGULO.')
else:
    print(f'As retas {l1}, {l2} e {l3} NÃO podem formar um TRIÂNGULO.')