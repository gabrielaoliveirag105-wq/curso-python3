print('----- DESAFIO 38 ------')
"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

from time import sleep
print('----- COMPARANDO NÚMEROS INTEIROS ------')
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

print('-'*40)
print('Comparando os números...')
print('-'*40)
sleep(1)

if n1 == n2:
    print(f'O primeiro e o segundo números são \033[1;32miguais.')
elif n1 > n2:
    print(f'O número {n1} é \033[1;32mmaior\033[m que o número {n2}.')
else:
    print(f'O número {n2} é \033[1;32mmaior\033[m que o número {n1}.')