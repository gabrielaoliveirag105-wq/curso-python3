print(' ----- DESAFIO 78 ----- ')
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

print('---- VALORES DENTRO DA LISTA ----')

valores = list()
maior = 0
menor = 0

for c in range(0,5):
    valores.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
       
print(f'\nOs valores da lista são: \033[1;33m{valores}\033[m')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}', end=' ')

print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}', end=' ')
print()

 