print('----- DESAFIO 42 ------')
""" Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

from time import sleep
sleep(1.0)

print('----- CÁLCULO TRIÂNGULO ------')
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print(f'As retas {l1}, {l2} e {l3} PODEM FORMAR um TRIÂNGULO.')
    if l1 == l2 == l3: # Uma condição entra dentro da outra (if dentro de if).
        print('O triâgulo formado é EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triângulo formado é ISÓSCELES.')
    elif l1 != l2 != l3:
        print('O triângulo formado é ESCALENO.')
else:
    print(f'As retas {l1}, {l2} e {l3} NÃO PODEM FORMAR um TRIÂNGULO.')
