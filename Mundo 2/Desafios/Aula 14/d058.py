print('----- DESAFIO 58 ------')
# Melhorando o desafio 28
# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuŕio tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
sleep(1.0)

c = 0 
paplpite = 0

print('-'*60)
print('     VAMOS JOGAR?     ')
print('Estou pensando em um número entre 0 e 10.... Tente adivinhar!')
print('-'*60)

computador = randint(0,10)
jogador = int(input('Em que número eu pensei? '))

while jogador != computador:
    print('\n\033[1;31mAinda não acertou, tente novamente.\033[m')
    jogador = int(input('Em que número eu pensei: '))
    c = c + 1
    paplpite = paplpite + 1

    if (jogador == computador):
        print(f'\033[1;32m\nParabéns, eu pensei exatamente no número {computador} e você ganhou.\033[m')
    else:
        print(f'Eu sou ótimo nesse jogo...')
print(f'\033[4;33mForam necessários {paplpite} palpites para você me vencer.\033[m')