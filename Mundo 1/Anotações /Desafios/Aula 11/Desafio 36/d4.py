print('------ DESAFIO 36 ------')
# Pegue alguns desafios dos 30 que foi passado e adicione cores.

# Crie um programa que leia um número inteiro na tela, e mostre se ele é PAR ou ÍMPAR.

from time import sleep
sleep(1.0)

print('\033[1;33m------ PAR OU ÍMPAR -------\033[m')
num = int(input('Escolha um número inteiro: '))

if (num % 2 == 0):
    print(f'O número \033[1;34m{num}\033[m é \033[4mPAR\033[m.')
else:
    print(f'O número \033[1;34m{num}\033[m é \033[4mÍMPAR\033[m.')
