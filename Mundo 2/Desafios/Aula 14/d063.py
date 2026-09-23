print('----- DESAFIO 63 ------')
"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8"""

print('\n === SEQUÊNCIA DE FIBONACCI === ')
n = int(input('Quantos termos voê deseja mostrar? '))
primeiro = 0
segundo = 1
c = 3
 
print(primeiro, end=' -> ')
print(segundo, end=' -> ')

while c <= n:
    terceiro = primeiro + segundo    
    print (terceiro, end=' -> ')
    primeiro = segundo
    segundo = terceiro
    c = c + 1
print('FIM')
print('\nPrograma finalizado!')