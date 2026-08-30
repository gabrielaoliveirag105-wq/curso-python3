print('------ DESAFIO 36 ------')
# Pegue alguns desafios dos 30 que foi passado e adicione cores.

# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuŕio tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
sleep(1.0)

print('-'*60)
print('\033[1;34m     VAMOS JOGAR?     \033[m')
print('\033[4;34mEstou pensando em um número entre 0 e 5.... Tente adivinhar!\033[m')
print('-'*60)

computador = randint(0,5)
jogador = int(input('Em que número eu pensei? '))

if (jogador == computador):
    print(f'\033[1;32mParabéns, eu pensei exatamente no número {computador} e você ganhou. \nVamos de novo que agora eu vou ganhar!\033[m')
else:
    print(f'\033[1;31mEu sou ótimo nesse jogo, pensei no número {computador}.\033[m')
print('\033[33mJogue mais uma vez!\033[m')
