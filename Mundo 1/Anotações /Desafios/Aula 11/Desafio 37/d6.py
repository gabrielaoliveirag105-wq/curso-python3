print('------ DESAFIO 37 ------')
# Pegue alguns desafios e coloque um sistema de cores.

# Faça um programa que leia dois números e mostre a soma entre eles.
cores = {'limpa': '\033[m', 'azul':'\033[4;34m', 'vermelho': '\033[1;31m', 'verde':'\033[4;32m'}

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
soma = n1 + n2
print(f'A soma entre {cores["azul"]}{n1}{cores["limpa"]} e {cores["verde"]}{n2}{cores["limpa"]} é igual a {cores["vermelho"]}{soma}{cores["limpa"]}.')