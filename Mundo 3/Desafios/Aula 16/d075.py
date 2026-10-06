print(' ----- DESAFIO 75 ----- ')
'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

print('----- VERIFICANDO VALORES -----')
numeros =(int(input('Digite o 1° valor: ')),
    int(input('Digite o 2° valor: ')),
    int(input('Digite o 3° valor: ')),
    int(input('Digite o 4° valor: ')))

print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na  {numeros.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
