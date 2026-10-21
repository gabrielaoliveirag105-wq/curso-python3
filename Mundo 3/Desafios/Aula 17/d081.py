print(' ----- DESAFIO 81 ----- ')
'''Crie um programa que vai ler vários números e colocar em uma lista.
A) Quantos números foram digitados.                                                                  B) A lista de valores, ordenada de forma decrescente.                                                                C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break

print(f'\nAo todo foram digitados {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores da lista em ordem decrescente fica: {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi achado na lista!')