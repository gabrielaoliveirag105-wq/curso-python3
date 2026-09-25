print('----- DESAFIO 66 ------')
#  Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

from time import sleep
print(' === LENDO VALORES E SOMANDO ===  ')
n = c = s = 0

while True:
    n = int(input('Escolha um número: \033[1;31m[999 para parar]\033[m '))
    if n == 999:
        break
    c = c + 1
    s = s + n 

print('-' * 40)
sleep(1)
print(f'Ao todo foram digitados {c} valores. \nA soma deles vale {s}.')
