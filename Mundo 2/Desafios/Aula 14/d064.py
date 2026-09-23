print('----- DESAFIO 64 ------')
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print(' === SOMANDO VÁRIOS VALORES === ')

c = n = soma = 0
n = int(input(f'Digite um número: \033[1;31m[999 para parar]\033[m '))

while n != 999:
    soma = soma + n
    c = c + 1
    n = int(input(f'Digite um número: \033[1;31m[999 para parar]\033[m '))
print(f'\nAo todo foram digitados {c} números. ')
print(f'A soma de todos os valores é igual a {soma}')